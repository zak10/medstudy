<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-2xl font-bold text-neutral-900">My Health Data</h1>
      <p class="mt-1 text-neutral-600">
        Track your measurements and progress across all studies
      </p>
    </div>

    <!-- Filters -->
    <div class="mb-6 flex flex-wrap gap-4">
      <select
        v-model="selectedStudy"
        class="px-3 py-2 border border-neutral-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
      >
        <option value="all">All Studies</option>
        <option v-for="study in studies" :key="study.id" :value="study.id">
          {{ study.title }}
        </option>
      </select>

      <select
        v-model="timeRange"
        class="px-3 py-2 border border-neutral-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
      >
        <option value="1m">Last Month</option>
        <option value="3m">Last 3 Months</option>
        <option value="6m">Last 6 Months</option>
        <option value="1y">Last Year</option>
        <option value="all">All Time</option>
      </select>

      <select
        v-model="selectedMetric"
        class="px-3 py-2 border border-neutral-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
      >
        <option value="all">All Metrics</option>
        <option v-for="metric in metrics" :key="metric.id" :value="metric.id">
          {{ metric.name }}
        </option>
      </select>
    </div>

    <!-- Main Data Display -->
    <div class="space-y-6">
      <!-- Vitamin D Levels Card -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="flex justify-between items-start mb-6">
          <div>
            <h3 class="text-lg font-medium text-neutral-900">
              Vitamin D Levels
            </h3>
            <p class="text-sm text-neutral-500">Measured every 6 weeks</p>
          </div>
          <div class="text-right">
            <div class="text-2xl font-semibold text-neutral-900">54 ng/mL</div>
            <div class="text-sm text-green-600">↑ 12 from baseline</div>
          </div>
        </div>

        <!-- Chart -->
        <div class="h-64 mb-4">
          <Line :data="vitaminDData" :options="chartOptions" />
        </div>

        <!-- Reference Range -->
        <div class="flex items-center justify-between text-sm text-neutral-600">
          <span>Target Range: 40-60 ng/mL</span>
          <span>Last Updated: Dec 15, 2024</span>
        </div>
      </div>

      <!-- Sleep Quality Card -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="flex justify-between items-start mb-6">
          <div>
            <h3 class="text-lg font-medium text-neutral-900">
              Sleep Quality Score
            </h3>
            <p class="text-sm text-neutral-500">Daily measurements</p>
          </div>
          <div class="text-right">
            <div class="text-2xl font-semibold text-neutral-900">8.2/10</div>
            <div class="text-sm text-green-600">↑ 1.4 from baseline</div>
          </div>
        </div>

        <!-- Chart -->
        <div class="h-64 mb-4">
          <LineChart :data="sleepData" :options="chartOptions" />
        </div>
      </div>

      <!-- Detailed Data Table -->
      <div class="bg-white rounded-lg shadow-sm overflow-hidden">
        <div class="px-6 py-4 border-b border-neutral-200">
          <h3 class="text-lg font-medium text-neutral-900">Data History</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-neutral-200">
            <thead class="bg-neutral-50">
              <tr>
                <th
                  class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase"
                >
                  Date
                </th>
                <th
                  class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase"
                >
                  Metric
                </th>
                <th
                  class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase"
                >
                  Value
                </th>
                <th
                  class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase"
                >
                  Study
                </th>
                <th
                  class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase"
                >
                  Notes
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-neutral-200">
              <tr v-for="entry in dataHistory" :key="entry.id">
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-neutral-900"
                >
                  {{ entry.date }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-neutral-900"
                >
                  {{ entry.metric }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-neutral-900"
                >
                  {{ entry.value }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm text-neutral-500"
                >
                  {{ entry.study }}
                </td>
                <td class="px-6 py-4 text-sm text-neutral-500">
                  {{ entry.notes }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Export Options -->
      <div class="flex justify-end space-x-4">
        <button
          class="px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50"
        >
          Download CSV
        </button>
        <button
          class="px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50"
        >
          Export Report
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const selectedStudy = ref("all");
const timeRange = ref("3m");
const selectedMetric = ref("all");

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
    },
  },
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};

const vitaminDData = {
  labels: ["Oct", "Nov", "Dec"],
  datasets: [
    {
      label: "Vitamin D (ng/mL)",
      data: [32, 45, 54],
      borderColor: "rgb(59, 130, 246)",
      tension: 0.1,
    },
  ],
};

const sleepData = {
  labels: Array.from({ length: 30 }, (_, i) => i + 1),
  datasets: [
    {
      label: "Sleep Quality",
      data: Array.from({ length: 30 }, () => Math.random() * 3 + 7),
      borderColor: "rgb(59, 130, 246)",
      tension: 0.1,
    },
  ],
};

const dataHistory = [
  {
    id: 1,
    date: "2024-12-15",
    metric: "Vitamin D",
    value: "54 ng/mL",
    study: "Vitamin D Optimization",
    notes: "Post-supplementation",
  },
  {
    id: 2,
    date: "2024-12-14",
    metric: "Sleep Quality",
    value: "8.5/10",
    study: "Magnesium & Sleep",
    notes: "Improved sleep latency",
  },
  // Add more history entries
];

const studies = [
  { id: 1, title: "Vitamin D Optimization" },
  { id: 2, title: "Magnesium & Sleep Quality" },
];

const metrics = [
  { id: "vitaminD", name: "Vitamin D Levels" },
  { id: "sleep", name: "Sleep Quality" },
];
</script>
