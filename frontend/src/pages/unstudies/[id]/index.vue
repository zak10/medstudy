<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Back Button -->
    <div class="mb-6">
      <button
        @click="$router.back()"
        class="flex items-center text-sm text-neutral-600 hover:text-primary-600"
      >
        <svg
          class="w-5 h-5 mr-1"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 19l-7-7 7-7"
          />
        </svg>
        Back to Studies
      </button>
    </div>

    <!-- Study Header -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <h1 class="text-3xl font-bold text-neutral-900">{{ study.title }}</h1>
        <button
          v-if="study.status === 'recruiting'"
          class="px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
        >
          Join Study
        </button>
      </div>

      <div class="mt-4 flex items-center space-x-4">
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
        <span class="text-sm text-neutral-600"
          >{{ study.participants }} participants</span
        >
        <span class="text-sm text-neutral-600">{{ study.duration }} weeks</span>
      </div>
    </div>

    <!-- Main Content -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Left Column - Main Study Info -->
      <div class="lg:col-span-2 space-y-8">
        <!-- Overview Section -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-xl font-semibold mb-4">Overview</h2>
          <p class="text-neutral-600">{{ study.description }}</p>

          <!-- Key Information -->
          <div class="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="flex items-center">
              <svg
                class="h-5 w-5 text-neutral-400 mr-2"
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
              <span class="text-sm text-neutral-600">
                Start Date: {{ study.startDate }}
              </span>
            </div>
            <div class="flex items-center">
              <svg
                class="h-5 w-5 text-neutral-400 mr-2"
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
              <span class="text-sm text-neutral-600">
                Led by: {{ study.institution }}
              </span>
            </div>
          </div>
        </div>

        <!-- Protocol Section -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-xl font-semibold mb-4">Protocol</h2>

          <!-- Timeline -->
          <div class="mb-6">
            <h3 class="text-lg font-medium mb-3">Timeline</h3>
            <div class="space-y-4">
              <div
                v-for="(phase, index) in study.protocol.timeline"
                :key="index"
                class="flex"
              >
                <div class="flex flex-col items-center mr-4">
                  <div
                    class="w-8 h-8 bg-primary-100 rounded-full flex items-center justify-center"
                  >
                    <span class="text-primary-600 font-medium">{{
                      index + 1
                    }}</span>
                  </div>
                  <div
                    class="h-full w-0.5 bg-primary-100"
                    v-if="index !== study.protocol.timeline.length - 1"
                  ></div>
                </div>
                <div class="pb-4">
                  <h4 class="text-base font-medium text-neutral-900">
                    {{ phase.title }}
                  </h4>
                  <p class="text-sm text-neutral-600">
                    {{ phase.description }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Requirements -->
          <div>
            <h3 class="text-lg font-medium mb-3">Requirements</h3>
            <ul class="list-disc list-inside space-y-2 text-neutral-600">
              <li v-for="req in study.protocol.requirements" :key="req">
                {{ req }}
              </li>
            </ul>
          </div>
        </div>

        <!-- Data Collection -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-xl font-semibold mb-4">Data Collection</h2>
          <div class="space-y-4">
            <div v-for="(item, index) in study.dataCollection" :key="index">
              <h3 class="text-base font-medium text-neutral-900">
                {{ item.title }}
              </h3>
              <p class="text-sm text-neutral-600">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column - Stats & Updates -->
      <div class="space-y-6">
        <!-- Study Stats -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-lg font-semibold mb-4">Study Statistics</h2>
          <div class="space-y-4">
            <div class="flex justify-between">
              <span class="text-neutral-600">Total Participants</span>
              <span class="font-medium">{{ study.participants }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-neutral-600">Completion Rate</span>
              <span class="font-medium">{{ study.completionRate }}%</span>
            </div>
            <div class="flex justify-between">
              <span class="text-neutral-600">Start Date</span>
              <span class="font-medium">{{ study.startDate }}</span>
            </div>
          </div>
        </div>

        <!-- Recent Updates -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-lg font-semibold mb-4">Recent Updates</h2>
          <div class="space-y-4">
            <div
              v-for="update in study.updates"
              :key="update.date"
              class="pb-4 border-b border-neutral-200 last:border-0"
            >
              <p class="text-sm text-neutral-600">{{ update.content }}</p>
              <span class="text-xs text-neutral-500">{{ update.date }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();
// Sample data - replace with actual API call
const study = {
  id: 1,
  title: "Vitamin D Optimization Protocol",
  description:
    "A comprehensive investigation into the effects of different Vitamin D supplementation strategies on blood levels and overall well-being. This study aims to identify optimal dosing patterns and their correlation with various health markers.",
  status: "recruiting",
  participants: 45,
  completionRate: 92,
  duration: 12,
  startDate: "Jan 15, 2024",
  institution: "Health Research Institute",

  protocol: {
    timeline: [
      {
        title: "Baseline Assessment",
        description: "Initial blood work and health questionnaire",
      },
      {
        title: "Supplementation Period",
        description: "12-week supplementation following assigned protocol",
      },
      {
        title: "Final Assessment",
        description: "Follow-up blood work and completion survey",
      },
    ],
    requirements: [
      "Age 18-65",
      "No current Vitamin D supplementation",
      "Ability to complete blood tests at specified intervals",
      "No history of hypercalcemia",
      "Commitment to follow protocol for 12 weeks",
    ],
  },

  dataCollection: [
    {
      title: "Blood Tests",
      description:
        "Vitamin D levels, calcium, and basic metabolic panel at 0, 6, and 12 weeks",
    },
    {
      title: "Weekly Check-ins",
      description:
        "Brief questionnaire about compliance and any noticed effects",
    },
    {
      title: "Final Report",
      description: "Comprehensive survey about experience and observed changes",
    },
  ],

  updates: [
    {
      content:
        "45th participant enrolled. Study continuing to show strong adherence rates.",
      date: "Feb 1, 2024",
    },
    {
      content:
        "Preliminary data showing interesting trends in absorption rates.",
      date: "Jan 25, 2024",
    },
    {
      content: "Study protocol update: Added optional mood tracking component.",
      date: "Jan 18, 2024",
    },
  ],
};
</script>
