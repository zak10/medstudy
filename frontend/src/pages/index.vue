<template>
  <div class="w-full py-12">
    <!-- Hero Section -->
    <div class="relative bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <!-- Main Hero Content -->
        <div class="relative pt-16 pb-8 text-center">
          <h1
            class="text-4xl font-bold text-neutral-900 sm:text-5xl md:text-6xl"
          >
            <span class="block">Community-Powered</span>
            <span class="block text-primary-600">Health Research</span>
          </h1>
          <p
            class="mt-3 max-w-md mx-auto text-base text-neutral-600 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl"
          >
            Join structured health studies designed by the community, for the
            community. Discover what really works.
          </p>
          <div class="mt-5 max-w-md mx-auto flex justify-center md:mt-8">
            <RouterLink
              to="/explore"
              class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700"
            >
              Start Exploring Studies
            </RouterLink>
          </div>
        </div>

        <!-- Process Steps -->
        <div class="max-w-5xl mx-auto px-4 pb-16">
          <div class="grid grid-cols-1 gap-8 md:grid-cols-4">
            <!-- Step 1 -->
            <div class="relative">
              <div class="bg-primary-50 rounded-lg p-6 text-center h-full">
                <div
                  class="absolute -top-3 -left-3 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold"
                >
                  1
                </div>
                <svg
                  class="w-8 h-8 text-primary-600 mx-auto mb-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
                  />
                </svg>
                <h3 class="text-lg font-semibold text-neutral-900 mb-2">
                  Choose Protocol
                </h3>
                <p class="text-sm text-neutral-600">
                  Select from community-designed research protocols with clear
                  guidelines
                </p>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="relative">
              <div class="bg-primary-50 rounded-lg p-6 text-center h-full">
                <div
                  class="absolute -top-3 -left-3 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold"
                >
                  2
                </div>
                <svg
                  class="w-8 h-8 text-primary-600 mx-auto mb-4"
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
                <h3 class="text-lg font-semibold text-neutral-900 mb-2">
                  Track Progress
                </h3>
                <p class="text-sm text-neutral-600">
                  Follow the protocol and log your data using standardized
                  measurements
                </p>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="relative">
              <div class="bg-primary-50 rounded-lg p-6 text-center h-full">
                <div
                  class="absolute -top-3 -left-3 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold"
                >
                  3
                </div>
                <svg
                  class="w-8 h-8 text-primary-600 mx-auto mb-4"
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
                <h3 class="text-lg font-semibold text-neutral-900 mb-2">
                  Share Results
                </h3>
                <p class="text-sm text-neutral-600">
                  Contribute your findings to the community knowledge base
                </p>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="relative">
              <div class="bg-primary-50 rounded-lg p-6 text-center h-full">
                <div
                  class="absolute -top-3 -left-3 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold"
                >
                  4
                </div>
                <svg
                  class="w-8 h-8 text-primary-600 mx-auto mb-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                  />
                </svg>
                <h3 class="text-lg font-semibold text-neutral-900 mb-2">
                  See Insights
                </h3>
                <p class="text-sm text-neutral-600">
                  Access aggregated data and discover what works
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-gradient-to-b from-neutral-50 to-white py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Section Title -->
        <div class="text-center mb-16">
          <h2
            class="text-3xl font-bold tracking-tight text-neutral-900 sm:text-4xl"
          >
            Unlocking Health Research For Everyone
          </h2>
          <p class="mt-4 max-w-2xl mx-auto text-lg text-neutral-600">
            We're bridging the gap between traditional research and real-world
            health optimization
          </p>
        </div>

        <!-- Key Points Grid -->
        <div class="grid grid-cols-1 gap-12 lg:grid-cols-3 lg:gap-8">
          <!-- Democratizing Research -->
          <div class="space-y-4">
            <div
              class="bg-primary-50 rounded-lg p-2 w-12 h-12 flex items-center justify-center"
            >
              <svg
                class="w-6 h-6 text-primary-600"
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
            </div>
            <h3 class="text-xl font-semibold text-neutral-900">
              Filling Research Gaps
            </h3>
            <p class="text-neutral-600">
              Many promising supplements and interventions go unstudied due to
              lack of patent potential or financial incentives. We're changing
              that by enabling community-driven research.
            </p>
          </div>

          <!-- Community Driven -->
          <div class="space-y-4">
            <div
              class="bg-primary-50 rounded-lg p-2 w-12 h-12 flex items-center justify-center"
            >
              <svg
                class="w-6 h-6 text-primary-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-neutral-900">
              Power of Community
            </h3>
            <p class="text-neutral-600">
              By connecting self-experimenters with structured protocols and
              tools for data collection, we're creating a new model for
              discovering what really works.
            </p>
          </div>

          <!-- Data Driven -->
          <div class="space-y-4">
            <div
              class="bg-primary-50 rounded-lg p-2 w-12 h-12 flex items-center justify-center"
            >
              <svg
                class="w-6 h-6 text-primary-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                />
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-neutral-900">
              Evidence-Based Insights
            </h3>
            <p class="text-neutral-600">
              Turn individual experiments into collective knowledge through
              structured data collection, analysis, and open sharing of results.
            </p>
          </div>
        </div>

        <!-- Problem Statement -->
        <div
          class="mt-24 bg-white rounded-2xl shadow-sm border border-neutral-200 p-8"
        >
          <div class="max-w-3xl mx-auto">
            <h3 class="text-2xl font-bold text-neutral-900 mb-6">
              Why We Need Community Research
            </h3>
            <div class="space-y-6 text-neutral-600">
              <p>
                Traditional pharmaceutical research focuses primarily on
                patentable compounds, leaving many promising natural supplements
                and interventions understudied. This creates a significant gap
                in our understanding of accessible health optimizations.
              </p>
              <p>
                Many supplements widely used by health-conscious individuals
                lack robust human studies, despite showing promise in
                preliminary research. The current research model often
                overlooks:
              </p>
              <ul class="list-disc pl-5 space-y-2">
                <li>Natural compounds that can't be patented</li>
                <li>Supplement combinations and timing optimization</li>
                <li>Lifestyle interventions with limited profit potential</li>
                <li>
                  Population-specific responses to different interventions
                </li>
              </ul>
              <p class="mt-6">
                By creating a platform for structured, community-driven
                research, we can collectively build knowledge about these
                overlooked areas while maintaining scientific rigor through
                standardized protocols and data collection.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Features Section -->
    <div class="py-12 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:text-center">
          <h2
            class="text-base text-primary-600 font-semibold tracking-wide uppercase"
          >
            How It Works
          </h2>
          <p
            class="mt-2 text-3xl leading-8 font-bold tracking-tight text-neutral-900 sm:text-4xl"
          >
            Research Made Accessible
          </p>
        </div>

        <div class="mt-10">
          <div
            class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10"
          >
            <div class="relative">
              <dt>
                <div
                  class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-primary-500 text-white"
                >
                  <svg
                    class="h-6 w-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                </div>
                <p class="ml-16 text-lg leading-6 font-medium text-neutral-900">
                  Structured Protocols
                </p>
              </dt>
              <dd class="mt-2 ml-16 text-base text-neutral-500">
                Access standardized templates and guidelines for health
                interventions.
              </dd>
            </div>

            <div class="relative">
              <dt>
                <div
                  class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-primary-500 text-white"
                >
                  <svg
                    class="h-6 w-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                    />
                  </svg>
                </div>
                <p class="ml-16 text-lg leading-6 font-medium text-neutral-900">
                  Community Driven
                </p>
              </dt>
              <dd class="mt-2 ml-16 text-base text-neutral-500">
                Connect with others and share experiences in a supportive
                environment.
              </dd>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Active Studies Section -->
    <div class="py-12 bg-neutral-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:text-center mb-8">
          <h2 class="text-3xl font-bold tracking-tight text-neutral-900">
            Active Unstudies
          </h2>
          <p class="mt-4 max-w-2xl text-xl text-neutral-500 lg:mx-auto">
            Join these ongoing community-driven research initiatives
          </p>
        </div>

        <!-- Scrolling Studies List -->
        <div class="mt-6 grid gap-6 lg:grid-cols-3">
          <div
            v-for="study in activeStudies"
            :key="study.id"
            class="bg-white overflow-hidden shadow rounded-lg hover:shadow-lg transition-shadow duration-300"
          >
            <div class="px-4 py-5 sm:p-6">
              <h3 class="text-lg font-medium text-neutral-900">
                {{ study.title }}
              </h3>
              <p class="mt-1 text-sm text-neutral-500">
                {{ study.description }}
              </p>
              <div class="mt-4">
                <span
                  class="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium"
                  :class="
                    study.status === 'Recruiting'
                      ? 'bg-accent-100 text-accent-800'
                      : 'bg-secondary-100 text-secondary-800'
                  "
                >
                  {{ study.status }}
                </span>
              </div>
              <div class="mt-4 flex items-center text-sm text-neutral-500">
                <svg
                  class="flex-shrink-0 mr-1.5 h-5 w-5 text-neutral-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
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
            </div>
            <div class="bg-neutral-50 px-4 py-4 sm:px-6">
              <div class="text-sm">
                <a
                  href="#"
                  class="font-medium text-primary-600 hover:text-primary-500"
                >
                  Learn more<span class="ml-1">→</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const activeStudies = ref([
  {
    id: 1,
    title: "Vitamin D Optimization Protocol",
    description:
      "Investigating the effects of different Vitamin D supplementation strategies on blood levels and well-being.",
    status: "Recruiting",
    duration: 12,
  },
  {
    id: 2,
    title: "Magnesium & Sleep Quality",
    description:
      "Examining the impact of various magnesium forms on sleep quality and duration.",
    status: "Recruiting",
    duration: 8,
  },
  {
    id: 3,
    title: "Omega-3 Bioavailability",
    description:
      "Comparing the absorption rates of different omega-3 supplement formulations.",
    status: "Active",
    duration: 16,
  },
]);
</script>
