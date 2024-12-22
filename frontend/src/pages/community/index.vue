researchers can use. Protocols Page Click to open website Copy Retry ZK let's
design the "propose new unstudy" page I'll create a multi-step form for
proposing a new unstudy, making it easy for users to input all necessary details
while maintaining clarity. Propose New Unstudy Form Click to open website Copy
Retry ZK okay lets now design the "community" section I'll create a community
section that combines forum-like discussions, Q&A, and study updates. Community
Page Click to open website Copy Retry Claude can make mistakes. Please
double-check responses. No file chosen 3.5 Sonnet Choose style Tip: Long chats
cause you to reach your usage limits faster. Start a new chat Community Page
Preview Code

<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Page Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-neutral-900">Community</h1>
      <p class="mt-2 text-lg text-neutral-600">
        Connect, share experiences, and discuss research with fellow
        participants
      </p>
    </div>

    <!-- Main Content Area -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Left Sidebar - Categories -->
      <div class="lg:col-span-1 space-y-6">
        <!-- Categories -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-lg font-semibold text-neutral-900 mb-4">
            Categories
          </h2>
          <nav class="space-y-2">
            <button
              v-for="category in categories"
              :key="category.id"
              @click="activeCategory = category.id"
              class="w-full flex items-center justify-between px-3 py-2 rounded-md text-left"
              :class="[
                activeCategory === category.id
                  ? 'bg-primary-50 text-primary-600'
                  : 'text-neutral-600 hover:bg-neutral-50',
              ]"
            >
              <span class="flex items-center">
                <component :is="category.icon" class="h-5 w-5 mr-2" />
                {{ category.name }}
              </span>
              <span class="text-sm text-neutral-500">{{ category.count }}</span>
            </button>
          </nav>
        </div>

        <!-- Active Studies -->
        <div class="bg-white rounded-lg shadow-sm p-6">
          <h2 class="text-lg font-semibold text-neutral-900 mb-4">
            Active Studies
          </h2>
          <div class="space-y-3">
            <a
              v-for="study in activeStudies"
              :key="study.id"
              href="#"
              class="block px-3 py-2 rounded-md hover:bg-neutral-50"
            >
              <div class="flex justify-between items-start">
                <span class="text-sm font-medium text-neutral-900">{{
                  study.title
                }}</span>
                <span class="text-xs text-neutral-500"
                  >{{ study.participants }} participants</span
                >
              </div>
              <span class="text-xs text-neutral-500"
                >Last active {{ study.lastActive }}</span
              >
            </a>
          </div>
        </div>
      </div>

      <!-- Main Content - Discussions -->
      <div class="lg:col-span-2">
        <!-- Action Bar -->
        <div class="mb-6 flex justify-between items-center">
          <div class="relative flex-1 max-w-lg">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Search discussions..."
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
          <button
            class="ml-4 px-4 py-2 bg-primary-600 text-white rounded-md hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            New Discussion
          </button>
        </div>

        <!-- Discussion List -->
        <div class="space-y-4">
          <div
            v-for="discussion in discussions"
            :key="discussion.id"
            class="bg-white rounded-lg shadow-sm border border-neutral-200 hover:border-neutral-300 transition-colors"
          >
            <div class="p-6">
              <!-- Discussion Header -->
              <div class="flex items-start justify-between mb-4">
                <div class="flex items-start space-x-4">
                  <img
                    :src="discussion.author.avatar"
                    :alt="discussion.author.name"
                    class="w-10 h-10 rounded-full"
                  />
                  <div>
                    <h3 class="text-lg font-medium text-neutral-900">
                      {{ discussion.title }}
                    </h3>
                    <p class="text-sm text-neutral-500">
                      Started by {{ discussion.author.name }} ·
                      {{ discussion.createdAt }}
                    </p>
                  </div>
                </div>
                <span
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                  :class="{
                    'bg-green-100 text-green-800':
                      discussion.type === 'question',
                    'bg-blue-100 text-blue-800':
                      discussion.type === 'study-update',
                    'bg-purple-100 text-purple-800':
                      discussion.type === 'discussion',
                  }"
                >
                  {{ discussion.type }}
                </span>
              </div>

              <!-- Discussion Preview -->
              <p class="text-neutral-600 mb-4">{{ discussion.preview }}</p>

              <!-- Discussion Footer -->
              <div
                class="flex items-center justify-between text-sm text-neutral-500"
              >
                <div class="flex space-x-4">
                  <span class="flex items-center">
                    <svg
                      class="h-5 w-5 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
                      />
                    </svg>
                    {{ discussion.replies }} replies
                  </span>
                  <span class="flex items-center">
                    <svg
                      class="h-5 w-5 mr-1"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                      />
                    </svg>
                    {{ discussion.views }} views
                  </span>
                </div>
                <div class="flex items-center">
                  <span class="text-neutral-500"
                    >Last reply {{ discussion.lastReply }}</span
                  >
                </div>
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

const searchQuery = ref("");
const activeCategory = ref("all");

// Sample data
const categories = [
  {
    id: "all",
    name: "All Topics",
    count: 234,
    icon: "svg-icon-all", // Replace with actual icon component
  },
  {
    id: "questions",
    name: "Questions & Help",
    count: 85,
    icon: "svg-icon-question",
  },
  {
    id: "studies",
    name: "Study Updates",
    count: 56,
    icon: "svg-icon-studies",
  },
  {
    id: "experiences",
    name: "Experiences",
    count: 93,
    icon: "svg-icon-experiences",
  },
];

const activeStudies = [
  {
    id: 1,
    title: "Vitamin D Optimization",
    participants: 45,
    lastActive: "2h ago",
  },
  {
    id: 2,
    title: "Magnesium & Sleep",
    participants: 32,
    lastActive: "4h ago",
  },
  {
    id: 3,
    title: "Omega-3 Bioavailability",
    participants: 28,
    lastActive: "6h ago",
  },
];

const discussions = [
  {
    id: 1,
    title: "Blood test timing for Vitamin D study",
    author: {
      name: "Sarah Chen",
      avatar: "/api/placeholder/40/40",
    },
    type: "question",
    preview:
      "I'm wondering about the optimal timing for blood tests in the Vitamin D study. Should they be taken at the same time of day?",
    replies: 12,
    views: 234,
    createdAt: "2 days ago",
    lastReply: "1h ago",
  },
  {
    id: 2,
    title: "Week 4 Update: Sleep Quality Improvements",
    author: {
      name: "Michael Rodriguez",
      avatar: "/api/placeholder/40/40",
    },
    type: "study-update",
    preview:
      "Sharing my experience with the magnesium protocol after 4 weeks. Sleep scores have improved significantly.",
    replies: 8,
    views: 156,
    createdAt: "1 day ago",
    lastReply: "3h ago",
  },
  {
    id: 3,
    title: "Protocol Modification Proposal",
    author: {
      name: "Emma Watson",
      avatar: "/api/placeholder/40/40",
    },
    type: "discussion",
    preview:
      "Based on recent research, I'd like to propose a modification to the current protocol. Here's my reasoning...",
    replies: 15,
    views: 312,
    createdAt: "3 days ago",
    lastReply: "30m ago",
  },
];
</script>
