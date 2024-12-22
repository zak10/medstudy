<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex items-center">
        <button
          @click="$router.back()"
          class="mr-4 text-neutral-600 hover:text-neutral-900"
        >
          <svg
            class="w-5 h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            />
          </svg>
        </button>
        <h1 class="text-3xl font-bold text-neutral-900">New Discussion</h1>
      </div>
      <p class="mt-2 text-lg text-neutral-600">
        Share your thoughts, questions, or updates with the community
      </p>
    </div>

    <!-- Form -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <form @submit.prevent="submitDiscussion" class="space-y-6">
        <!-- Discussion Type -->
        <div class="grid grid-cols-3 gap-4">
          <button
            v-for="type in discussionTypes"
            :key="type.id"
            type="button"
            @click="form.type = type.id"
            class="p-4 rounded-lg border-2 text-center focus:outline-none"
            :class="[
              form.type === type.id
                ? 'border-primary-500 bg-primary-50 text-primary-700'
                : 'border-neutral-200 hover:border-neutral-300',
            ]"
          >
            <div class="flex justify-center mb-2">
              <component :is="type.icon" class="h-6 w-6" />
            </div>
            <div class="font-medium">{{ type.name }}</div>
            <div class="text-sm text-neutral-500 mt-1">
              {{ type.description }}
            </div>
          </button>
        </div>

        <!-- Title -->
        <div>
          <label class="block text-sm font-medium text-neutral-700"
            >Title</label
          >
          <input
            v-model="form.title"
            type="text"
            class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
            placeholder="What would you like to discuss?"
          />
        </div>

        <!-- Related Study -->
        <div>
          <label class="block text-sm font-medium text-neutral-700"
            >Related Study (Optional)</label
          >
          <select
            v-model="form.relatedStudy"
            class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="">Select a study</option>
            <option v-for="study in studies" :key="study.id" :value="study.id">
              {{ study.title }}
            </option>
          </select>
        </div>

        <!-- Content -->
        <div>
          <label class="block text-sm font-medium text-neutral-700"
            >Content</label
          >
          <!-- Simple toolbar -->
          <div
            class="mt-1 border border-neutral-300 rounded-t-md bg-neutral-50 px-3 py-2 flex space-x-2"
          >
            <button
              v-for="tool in textTools"
              :key="tool.id"
              type="button"
              class="p-1 rounded hover:bg-neutral-200"
              :class="{ 'bg-neutral-200': tool.active }"
            >
              <component :is="tool.icon" class="w-4 h-4 text-neutral-700" />
            </button>
          </div>
          <textarea
            v-model="form.content"
            rows="12"
            class="block w-full px-3 py-2 border border-t-0 border-neutral-300 rounded-b-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
            placeholder="Share your thoughts..."
          ></textarea>
        </div>

        <!-- Tags -->
        <div>
          <label class="block text-sm font-medium text-neutral-700">Tags</label>
          <div class="mt-1 flex flex-wrap gap-2">
            <span
              v-for="tag in form.tags"
              :key="tag"
              class="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm bg-neutral-100 text-neutral-800"
            >
              {{ tag }}
              <button
                type="button"
                @click="removeTag(tag)"
                class="ml-1 text-neutral-600 hover:text-neutral-900"
              >
                <svg
                  class="h-4 w-4"
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
            </span>
            <input
              v-model="newTag"
              @keydown.enter.prevent="addTag"
              type="text"
              class="inline-flex items-center px-3 py-1 border border-neutral-300 rounded-full text-sm focus:outline-none focus:ring-1 focus:ring-primary-500"
              placeholder="Add a tag..."
            />
          </div>
        </div>

        <!-- Actions -->
        <div class="flex justify-end space-x-4">
          <button
            type="button"
            @click="previewMode = !previewMode"
            class="px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            {{ previewMode ? "Edit" : "Preview" }}
          </button>
          <button
            type="submit"
            class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
          >
            Post Discussion
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";

const previewMode = ref(false);
const newTag = ref("");

const form = reactive({
  type: "discussion",
  title: "",
  relatedStudy: "",
  content: "",
  tags: [],
});

const discussionTypes = [
  {
    id: "discussion",
    name: "Discussion",
    description: "Start a general discussion about research or findings",
    icon: "ChatIcon",
  },
  {
    id: "question",
    name: "Question",
    description: "Ask for help or clarification about protocols",
    icon: "QuestionIcon",
  },
  {
    id: "update",
    name: "Study Update",
    description: "Share progress or results from your study",
    icon: "ChartIcon",
  },
];

const studies = [
  { id: 1, title: "Vitamin D Optimization Protocol" },
  { id: 2, title: "Magnesium & Sleep Quality Study" },
  { id: 3, title: "Omega-3 Bioavailability Research" },
];

const textTools = [
  { id: "bold", icon: "BoldIcon", active: false },
  { id: "italic", icon: "ItalicIcon", active: false },
  { id: "link", icon: "LinkIcon", active: false },
  { id: "list", icon: "ListIcon", active: false },
  { id: "quote", icon: "QuoteIcon", active: false },
];

const addTag = () => {
  if (newTag.value.trim() && !form.tags.includes(newTag.value.trim())) {
    form.tags.push(newTag.value.trim());
    newTag.value = "";
  }
};

const removeTag = (tag) => {
  form.tags = form.tags.filter((t) => t !== tag);
};

const submitDiscussion = async () => {
  // Add your submission logic here
  console.log("Submitting discussion:", form);
};
</script>
