<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-neutral-900">Research Protocols</h1>
      <p class="mt-2 text-lg text-neutral-600">
        Standardized templates and guidelines for conducting health research
      </p>
    </div>

    <!-- Category Tabs -->
    <div class="mb-8 border-b border-neutral-200">
      <nav class="-mb-px flex space-x-8">
        <button
          v-for="category in categories"
          :key="category.id"
          @click="activeCategory = category.id"
          class="whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm"
          :class="[
            activeCategory === category.id
              ? 'border-primary-500 text-primary-600'
              : 'border-transparent text-neutral-500 hover:text-neutral-700 hover:border-neutral-300',
          ]"
        >
          {{ category.name }}
        </button>
      </nav>
    </div>

    <!-- Search and Filters -->
    <div class="mb-8">
      <div class="relative max-w-lg">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Search protocols..."
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
    </div>

    <!-- Protocols Grid -->
    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="protocol in filteredProtocols"
        :key="protocol.id"
        class="bg-white rounded-lg shadow-sm border border-neutral-200 hover:shadow-md transition-shadow duration-200"
      >
        <div class="p-6">
          <!-- Protocol Header -->
          <div class="flex items-start justify-between mb-4">
            <div>
              <h3 class="text-lg font-semibold text-neutral-900">
                {{ protocol.title }}
              </h3>
              <p class="text-sm text-neutral-600 mt-1">
                {{ protocol.description }}
              </p>
            </div>
            <span
              class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-100 text-primary-800"
            >
              {{ protocol.complexity }}
            </span>
          </div>

          <!-- Protocol Details -->
          <div class="space-y-3 mb-4">
            <div class="flex items-center text-sm text-neutral-600">
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
              Duration: {{ protocol.duration }}
            </div>
            <div class="flex items-center text-sm text-neutral-600">
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
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              {{ protocol.validationStatus }}
            </div>
            <div class="flex items-center text-sm text-neutral-600">
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
                  d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              {{ protocol.completedStudies }} completed studies
            </div>
          </div>

          <!-- Tags -->
          <div class="mb-4">
            <div class="flex flex-wrap gap-2">
              <span
                v-for="tag in protocol.tags"
                :key="tag"
                class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-neutral-100 text-neutral-800"
              >
                {{ tag }}
              </span>
            </div>
          </div>

          <!-- Actions -->
          <div class="flex space-x-3">
            <button
              class="flex-1 inline-flex items-center justify-center px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              Preview
            </button>
            <button
              class="flex-1 inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
            >
              Use Template
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

const searchQuery = ref("");
const activeCategory = ref("all");

const categories = [
  { id: "all", name: "All Protocols" },
  { id: "supplements", name: "Supplements" },
  { id: "lifestyle", name: "Lifestyle" },
  { id: "nutrition", name: "Nutrition" },
  { id: "exercise", name: "Exercise" },
];

// Sample data - replace with actual API call
const protocols = [
  {
    id: 1,
    title: "Supplement Efficacy Protocol",
    description:
      "Standardized template for testing supplement effectiveness with controlled variables.",
    complexity: "Intermediate",
    duration: "8-12 weeks",
    validationStatus: "Peer Reviewed",
    completedStudies: 24,
    category: "supplements",
    tags: ["Biomarkers", "Blood Tests", "Controlled"],
  },
  {
    id: 2,
    title: "Sleep Optimization Protocol",
    description:
      "Framework for studying sleep quality interventions and tracking outcomes.",
    complexity: "Basic",
    duration: "4-6 weeks",
    validationStatus: "Community Tested",
    completedStudies: 15,
    category: "lifestyle",
    tags: ["Sleep", "Wellness", "Tracking"],
  },
  {
    id: 3,
    title: "Nutrient Absorption Study",
    description:
      "Template for measuring nutrient absorption rates and bioavailability.",
    complexity: "Advanced",
    duration: "12-16 weeks",
    validationStatus: "Expert Reviewed",
    completedStudies: 8,
    category: "nutrition",
    tags: ["Bioavailability", "Blood Tests", "Nutrition"],
  },
  // Add more protocols as needed
];

const filteredProtocols = computed(() => {
  return protocols.filter((protocol) => {
    // Category filter
    if (
      activeCategory.value !== "all" &&
      protocol.category !== activeCategory.value
    ) {
      return false;
    }

    // Search filter
    if (
      searchQuery.value &&
      !protocol.title.toLowerCase().includes(searchQuery.value.toLowerCase())
    ) {
      return false;
    }

    return true;
  });
});
</script>
