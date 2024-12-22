<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Welcome Header -->
    <div class="mb-8">
      <h1 class="text-2xl font-bold text-neutral-900">
        Welcome back, {{ user.firstName }}
      </h1>
      <p class="mt-1 text-neutral-600">
        Track your research journey and manage your studies
      </p>
    </div>

    <!-- Quick Stats -->
    <div class="grid grid-cols-1 gap-4 sm:grid-cols-4 mb-8">
      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="text-sm text-neutral-600">Active Studies</div>
        <div class="mt-2 flex items-baseline">
          <div class="text-2xl font-semibold text-neutral-900">2</div>
          <div class="ml-2 text-sm text-green-600">On Track</div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="text-sm text-neutral-600">Completed Studies</div>
        <div class="mt-2 flex items-baseline">
          <div class="text-2xl font-semibold text-neutral-900">3</div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="text-sm text-neutral-600">Data Points Logged</div>
        <div class="mt-2 flex items-baseline">
          <div class="text-2xl font-semibold text-neutral-900">147</div>
          <div class="ml-2 text-sm text-neutral-500">Total</div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="text-sm text-neutral-600">Protocol Adherence</div>
        <div class="mt-2 flex items-baseline">
          <div class="text-2xl font-semibold text-neutral-900">94%</div>
          <div class="ml-2 text-sm text-green-600">↑ 2%</div>
        </div>
      </div>
    </div>

    <!-- Active Studies -->
    <div class="mb-12">
      <h2 class="text-xl font-semibold text-neutral-900 mb-4">
        Active Studies
      </h2>
      <div class="grid gap-6 grid-cols-1 lg:grid-cols-2">
        <div
          v-for="study in activeStudies"
          :key="study.id"
          class="bg-white rounded-lg shadow-sm border border-neutral-200"
        >
          <div class="p-6">
            <div class="flex justify-between items-start mb-4">
              <div>
                <h3 class="text-lg font-medium text-neutral-900">
                  {{ study.title }}
                </h3>
                <p class="text-sm text-neutral-600">
                  Week {{ study.currentWeek }} of {{ study.totalWeeks }}
                </p>
              </div>
              <span
                class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                :class="
                  study.status === 'on-track'
                    ? 'bg-green-100 text-green-800'
                    : 'bg-yellow-100 text-yellow-800'
                "
              >
                {{ study.status === "on-track" ? "On Track" : "Action Needed" }}
              </span>
            </div>

            <!-- Progress Bar -->
            <div class="w-full bg-neutral-100 rounded-full h-2.5 mb-4">
              <div
                class="bg-primary-600 h-2.5 rounded-full"
                :style="{
                  width: `${(study.currentWeek / study.totalWeeks) * 100}%`,
                }"
              ></div>
            </div>

            <!-- Next Tasks -->
            <div class="space-y-3 mb-4">
              <h4 class="text-sm font-medium text-neutral-900">
                Upcoming Tasks
              </h4>
              <div
                v-for="task in study.upcomingTasks"
                :key="task.id"
                class="flex items-center"
              >
                <div
                  class="w-2 h-2 rounded-full mr-2"
                  :class="task.urgent ? 'bg-red-500' : 'bg-neutral-300'"
                ></div>
                <span class="text-sm text-neutral-600">{{
                  task.description
                }}</span>
                <span class="text-xs text-neutral-500 ml-auto">{{
                  task.due
                }}</span>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex space-x-3">
              <button
                class="flex-1 inline-flex justify-center items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700"
              >
                Log Data
              </button>
              <button
                class="flex-1 inline-flex justify-center items-center px-4 py-2 border border-neutral-300 text-sm font-medium rounded-md text-neutral-700 bg-white hover:bg-neutral-50"
              >
                View Details
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Study History -->
    <div>
      <h2 class="text-xl font-semibold text-neutral-900 mb-4">Study History</h2>
      <div class="bg-white rounded-lg shadow-sm overflow-hidden">
        <table class="min-w-full divide-y divide-neutral-200">
          <thead class="bg-neutral-50">
            <tr>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider"
              >
                Study
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider"
              >
                Duration
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider"
              >
                Completion
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider"
              >
                Status
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-neutral-500 uppercase tracking-wider"
              >
                Results
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-neutral-200">
            <tr v-for="study in completedStudies" :key="study.id">
              <td class="px-6 py-4">
                <div class="text-sm font-medium text-neutral-900">
                  {{ study.title }}
                </div>
                <div class="text-sm text-neutral-500">{{ study.date }}</div>
              </td>
              <td class="px-6 py-4 text-sm text-neutral-600">
                {{ study.duration }}
              </td>
              <td class="px-6 py-4">
                <div class="text-sm text-neutral-900">
                  {{ study.completion }}%
                </div>
                <div class="text-xs text-neutral-500">Protocol Adherence</div>
              </td>
              <td class="px-6 py-4">
                <span
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                  :class="
                    study.status === 'completed'
                      ? 'bg-green-100 text-green-800'
                      : 'bg-red-100 text-red-800'
                  "
                >
                  {{ study.status }}
                </span>
              </td>
              <td class="px-6 py-4">
                <button
                  class="text-primary-600 hover:text-primary-900 text-sm font-medium"
                >
                  View Report
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const user = {
  firstName: "Alex",
};

const activeStudies = [
  {
    id: 1,
    title: "Vitamin D Optimization Protocol",
    currentWeek: 4,
    totalWeeks: 12,
    status: "on-track",
    upcomingTasks: [
      { id: 1, description: "Blood Test Due", due: "Tomorrow", urgent: true },
      { id: 2, description: "Weekly Survey", due: "In 3 days", urgent: false },
    ],
  },
  {
    id: 2,
    title: "Magnesium & Sleep Quality Study",
    currentWeek: 2,
    totalWeeks: 8,
    status: "needs-attention",
    upcomingTasks: [
      { id: 3, description: "Sleep Log Entry", due: "Today", urgent: true },
      {
        id: 4,
        description: "Protocol Check-in",
        due: "Next week",
        urgent: false,
      },
    ],
  },
];

const completedStudies = [
  {
    id: 1,
    title: "Omega-3 Bioavailability Study",
    date: "Completed Oct 2024",
    duration: "12 weeks",
    completion: 98,
    status: "completed",
  },
  {
    id: 2,
    title: "Zinc & Immune Function Protocol",
    date: "Completed Aug 2024",
    duration: "8 weeks",
    completion: 92,
    status: "completed",
  },
  {
    id: 3,
    title: "Circadian Rhythm Optimization",
    date: "Completed Jun 2024",
    duration: "6 weeks",
    completion: 85,
    status: "completed",
  },
];
</script>
