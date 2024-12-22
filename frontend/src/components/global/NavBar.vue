<template>
  <nav class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <!-- Left side - Logo and main nav -->
        <div class="flex">
          <!-- Logo -->
          <div class="flex-shrink-0 flex items-center">
            <RouterLink to="/" class="flex items-center">
              <svg
                class="h-8 w-8 text-primary-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"
                />
              </svg>
              <span class="ml-2 text-xl font-bold text-primary-600"
                >Unstudy</span
              >
            </RouterLink>
          </div>

          <!-- Main Navigation -->
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <RouterLink
              to="/explore"
              class="inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
              :class="[
                $route.path === '/explore'
                  ? 'border-primary-500 text-neutral-900'
                  : 'border-transparent text-neutral-500 hover:border-neutral-300 hover:text-neutral-700',
              ]"
            >
              Explore Studies
            </RouterLink>
            <RouterLink
              to="/protocols"
              class="inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
              :class="[
                $route.path === '/protocols'
                  ? 'border-primary-500 text-neutral-900'
                  : 'border-transparent text-neutral-500 hover:border-neutral-300 hover:text-neutral-700',
              ]"
            >
              Protocols
            </RouterLink>
            <RouterLink
              to="/community"
              class="inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
              :class="[
                $route.path === '/community'
                  ? 'border-primary-500 text-neutral-900'
                  : 'border-transparent text-neutral-500 hover:border-neutral-300 hover:text-neutral-700',
              ]"
            >
              Community
            </RouterLink>
          </div>
        </div>

        <!-- Right side - Auth buttons -->
        <div class="hidden sm:ml-6 sm:flex sm:items-center sm:space-x-4">
          <RouterLink
            to="/login"
            class="text-neutral-500 hover:text-neutral-700 px-3 py-2 text-sm font-medium"
          >
            Log in
          </RouterLink>
        </div>

        <!-- Mobile menu button -->
        <div class="flex items-center sm:hidden">
          <button
            @click="isOpen = !isOpen"
            class="inline-flex items-center justify-center p-2 rounded-md text-neutral-400 hover:text-neutral-500 hover:bg-neutral-100"
            aria-expanded="false"
          >
            <span class="sr-only">Open main menu</span>
            <!-- Icon when menu is closed -->
            <svg
              v-if="!isOpen"
              class="block h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
            <!-- Icon when menu is open -->
            <svg
              v-else
              class="block h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div v-show="isOpen" class="sm:hidden">
      <div class="pt-2 pb-3 space-y-1">
        <RouterLink
          to="/explore"
          class="block pl-3 pr-4 py-2 border-l-4 text-base font-medium"
          :class="[
            $route.path === '/explore'
              ? 'bg-primary-50 border-primary-500 text-primary-700'
              : 'border-transparent text-neutral-500 hover:bg-neutral-50 hover:border-neutral-300 hover:text-neutral-700',
          ]"
          @click="isOpen = false"
        >
          Explore Studies
        </RouterLink>
        <RouterLink
          to="/protocols"
          class="block pl-3 pr-4 py-2 border-l-4 text-base font-medium"
          :class="[
            $route.path === '/protocols'
              ? 'bg-primary-50 border-primary-500 text-primary-700'
              : 'border-transparent text-neutral-500 hover:bg-neutral-50 hover:border-neutral-300 hover:text-neutral-700',
          ]"
          @click="isOpen = false"
        >
          Protocols
        </RouterLink>
        <RouterLink
          to="/community"
          class="block pl-3 pr-4 py-2 border-l-4 text-base font-medium"
          :class="[
            $route.path === '/community'
              ? 'bg-primary-50 border-primary-500 text-primary-700'
              : 'border-transparent text-neutral-500 hover:bg-neutral-50 hover:border-neutral-300 hover:text-neutral-700',
          ]"
          @click="isOpen = false"
        >
          Community
        </RouterLink>
      </div>
      <div class="pt-4 pb-3 border-t border-neutral-200">
        <div class="space-y-1">
          <RouterLink
            to="/login"
            class="block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium text-neutral-500 hover:bg-neutral-50 hover:border-neutral-300 hover:text-neutral-700"
            @click="isOpen = false"
          >
            Log in
          </RouterLink>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, RouterLink } from "vue-router";

const route = useRoute();
const isOpen = ref(false);
</script>
