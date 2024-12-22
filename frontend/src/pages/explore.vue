<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-neutral-900">Explore Studies</h1>
      <p class="mt-2 text-lg text-neutral-600">
        Discover and join ongoing research initiatives
      </p>
    </div>

    <!-- Search and Filters -->
    <div
      class="mb-8 space-y-4 sm:space-y-0 sm:flex sm:items-center sm:justify-between"
    >
      <!-- Search -->
      <div class="relative flex-1 max-w-lg">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Search studies..."
          class="w-full px-4 py-2 pl-10 pr-4 text-sm border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        />
        <div
          class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
        >
          <svg
            class="h-5 w-5 text-neutral-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
      </div>

      <!-- Filters -->
      <div class="flex space-x-4">
        <select
          v-model="statusFilter"
          class="block pl-3 pr-10 py-2 text-sm border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Statuses</option>
          <option value="recruiting">Recruiting</option>
          <option value="active">Active</option>
          <option value="completed">Completed</option>
        </select>

        <select
          v-model="durationFilter"
          class="block pl-3 pr-10 py-2 text-sm border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        >
          <option value="">All Durations</option>
          <option value="short">Short (< 4 weeks)</option>
          <option value="medium">Medium (4-12 weeks)</option>
          <option value="long">Long (> 12 weeks)</option>
        </select>
      </div>
    </div>

    <!-- Studies Grid -->
    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="study in filteredStudies"
        :key="study.id"
        class="bg-white rounded-lg shadow-sm border border-neutral-200 hover:shadow-md transition-shadow duration-200"
      >
        <div class="p-6">
          <!-- Study Status Badge -->
          <div class="flex justify-between items-start mb-4">
            <span
              class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
              :class="{
                'bg-green-100 text-green-800': study.status === 'recruiting',
                'bg-blue-100 text-blue-800': study.status === 'active',
                'bg-neutral-100 text-neutral-800': study.status === 'completed',
              }"
            >
              {{ study.status }}
            </span>
            <span class="text-sm text-neutral-500"
              >{{ study.participants }} participants</span
            >
          </div>

          <!-- Study Info -->
          <h3 class="text-lg font-semibold text-neutral-900 mb-2">
            {{ study.title }}
          </h3>
          <p class="text-neutral-600 text-sm mb-4">{{ study.description }}</p>

          <!-- Study Details -->
          <div class="space-y-2">
            <div class="flex items-center text-sm text-neutral-500">
              <svg
                class="h-5 w-5 mr-2 text-neutral-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              {{ study.duration }} weeks
            </div>
            <div class="flex items-center text-sm text-neutral-500">
              <svg
                class="h-5 w-5 mr-2 text-neutral-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
                />
              </svg>
              {{ study.institution }}
            </div>
          </div>

          <!-- Action Button -->
          <button
            class="mt-4 w-full inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            View Details
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

const searchQuery = ref("");
const statusFilter = ref("");
const durationFilter = ref("");

// Sample data - replace with actual API call
const studies = [
  {
    id: 1,
    title: "Vitamin D Optimization Protocol",
    description:
      "Investigating the effects of different Vitamin D supplementation strategies on blood levels and well-being.",
    status: "recruiting",
    duration: 12,
    participants: 45,
    institution: "Health Research Institute",
  },
  {
    id: 2,
    title: "Magnesium & Sleep Quality",
    description:
      "Examining the impact of various magnesium forms on sleep quality and duration.",
    status: "active",
    duration: 8,
    participants: 89,
    institution: "Sleep Science Center",
  },
  {
    id: 3,
    title: "Omega-3 Bioavailability Study",
    description:
      "Comparing the absorption rates of different omega-3 supplement formulations.",
    status: "completed",
    duration: 16,
    participants: 120,
    institution: "Nutrition Research Lab",
  },
  // Add more studies as needed
];

const filteredStudies = computed(() => {
  return studies.filter((study) => {
    // Search filter
    if (
      searchQuery.value &&
      !study.title.toLowerCase().includes(searchQuery.value.toLowerCase())
    ) {
      return false;
    }

    // Status filter
    if (statusFilter.value && study.status !== statusFilter.value) {
      return false;
    }

    // Duration filter
    if (durationFilter.value) {
      if (durationFilter.value === "short" && study.duration >= 4) return false;
      if (
        durationFilter.value === "medium" &&
        (study.duration < 4 || study.duration > 12)
      )
        return false;
      if (durationFilter.value === "long" && study.duration <= 12) return false;
    }

    return true;
  });
});
</script>
