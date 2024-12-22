<script setup lang="ts">
import { RouterView, RouterLink } from "vue-router";
import NavBar from "@/components/global/NavBar.vue";
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <NavBar />

    <main class="flex-1 w-full pb-12">
      <RouterView />
    </main>
  </div>

  <!-- Add padding to account for fixed navbar -->
</template>
