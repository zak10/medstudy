<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-neutral-900">Propose New Unstudy</h1>
      <p class="mt-2 text-lg text-neutral-600">
        Create a new community-driven research initiative
      </p>
    </div>

    <!-- Progress Steps -->
    <div class="mb-8">
      <div class="flex justify-between">
        <div v-for="(step, index) in steps" :key="step.id" class="flex-1">
          <div class="flex items-center">
            <div
              class="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center font-medium text-sm"
              :class="[
                currentStep > index
                  ? 'bg-primary-600 text-white'
                  : currentStep === index
                  ? 'bg-primary-100 text-primary-600 ring-2 ring-primary-600'
                  : 'bg-neutral-100 text-neutral-500',
              ]"
            >
              {{ index + 1 }}
            </div>
            <div
              v-if="index < steps.length - 1"
              class="flex-1 h-0.5 mx-2"
              :class="[
                currentStep > index ? 'bg-primary-600' : 'bg-neutral-200',
              ]"
            ></div>
          </div>
          <div class="mt-2">
            <span
              class="text-sm font-medium"
              :class="[
                currentStep >= index ? 'text-primary-600' : 'text-neutral-500',
              ]"
            >
              {{ step.name }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Form Steps -->
    <div class="bg-white shadow-sm rounded-lg p-6 mb-8">
      <!-- Basic Information -->
      <div v-if="currentStep === 0">
        <h2 class="text-xl font-semibold mb-6">Basic Information</h2>
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Study Title</label
            >
            <input
              v-model="form.title"
              type="text"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              placeholder="E.g., Vitamin D Optimization Protocol"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Category</label
            >
            <select
              v-model="form.category"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
            >
              <option value="supplements">Supplements</option>
              <option value="lifestyle">Lifestyle</option>
              <option value="nutrition">Nutrition</option>
              <option value="exercise">Exercise</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Description</label
            >
            <textarea
              v-model="form.description"
              rows="4"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              placeholder="Describe the purpose and goals of your study..."
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Duration (weeks)</label
            >
            <input
              v-model="form.duration"
              type="number"
              min="1"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
            />
          </div>
        </div>
      </div>

      <!-- Protocol Design -->
      <div v-if="currentStep === 1">
        <h2 class="text-xl font-semibold mb-6">Protocol Design</h2>
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Intervention Details</label
            >
            <textarea
              v-model="form.intervention"
              rows="4"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              placeholder="Describe the intervention in detail..."
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Required Measurements</label
            >
            <div class="mt-2 space-y-2">
              <div
                v-for="(measurement, index) in form.measurements"
                :key="index"
                class="flex gap-2"
              >
                <input
                  v-model="form.measurements[index]"
                  type="text"
                  class="flex-1 px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                  placeholder="E.g., Blood Vitamin D levels"
                />
                <button
                  @click="removeMeasurement(index)"
                  class="text-neutral-400 hover:text-neutral-500"
                >
                  <svg
                    class="h-5 w-5"
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
            <button
              @click="addMeasurement"
              class="mt-2 text-sm text-primary-600 hover:text-primary-500"
            >
              + Add measurement
            </button>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Timeline</label
            >
            <div class="mt-2 space-y-4">
              <div
                v-for="(phase, index) in form.timeline"
                :key="index"
                class="border border-neutral-200 rounded-md p-4"
              >
                <div class="flex justify-between items-start mb-2">
                  <input
                    v-model="phase.name"
                    type="text"
                    class="flex-1 px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                    placeholder="Phase name"
                  />
                  <button
                    @click="removePhase(index)"
                    class="ml-2 text-neutral-400 hover:text-neutral-500"
                  >
                    <svg
                      class="h-5 w-5"
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
                <textarea
                  v-model="phase.description"
                  rows="2"
                  class="w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                  placeholder="Phase description"
                ></textarea>
              </div>
              <button
                @click="addPhase"
                class="text-sm text-primary-600 hover:text-primary-500"
              >
                + Add phase
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Requirements & Safety -->
      <div v-if="currentStep === 2">
        <h2 class="text-xl font-semibold mb-6">Requirements & Safety</h2>
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Participant Requirements</label
            >
            <div class="mt-2 space-y-2">
              <div
                v-for="(req, index) in form.requirements"
                :key="index"
                class="flex gap-2"
              >
                <input
                  v-model="form.requirements[index]"
                  type="text"
                  class="flex-1 px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                  placeholder="E.g., Must be 18+ years old"
                />
                <button
                  @click="removeRequirement(index)"
                  class="text-neutral-400 hover:text-neutral-500"
                >
                  <svg
                    class="h-5 w-5"
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
            <button
              @click="addRequirement"
              class="mt-2 text-sm text-primary-600 hover:text-primary-500"
            >
              + Add requirement
            </button>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Exclusion Criteria</label
            >
            <div class="mt-2 space-y-2">
              <div
                v-for="(criteria, index) in form.exclusionCriteria"
                :key="index"
                class="flex gap-2"
              >
                <input
                  v-model="form.exclusionCriteria[index]"
                  type="text"
                  class="flex-1 px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                  placeholder="E.g., Currently taking medication X"
                />
                <button
                  @click="removeExclusionCriteria(index)"
                  class="text-neutral-400 hover:text-neutral-500"
                >
                  <svg
                    class="h-5 w-5"
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
            <button
              @click="addExclusionCriteria"
              class="mt-2 text-sm text-primary-600 hover:text-primary-500"
            >
              + Add exclusion criteria
            </button>
          </div>

          <div>
            <label class="block text-sm font-medium text-neutral-700"
              >Safety Monitoring</label
            >
            <textarea
              v-model="form.safetyMonitoring"
              rows="4"
              class="mt-1 block w-full px-3 py-2 border border-neutral-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              placeholder="Describe how participant safety will be monitored..."
            ></textarea>
          </div>
        </div>
      </div>
    </div>

    <!-- Navigation Buttons -->
    <div class="flex justify-between">
      <button
        v-if="currentStep > 0"
        @click="currentStep--"
        class="px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
      >
        Previous
      </button>
      <div class="flex-1"></div>
      <button
        v-if="currentStep < steps.length - 1"
        @click="currentStep++"
        class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
      >
        Next
      </button>
      <button
        v-else
        @click="submitForm"
        class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
      >
        Submit Proposal
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";

const currentStep = ref(0);
const steps = [
  { id: "basics", name: "Basic Information" },
  { id: "protocol", name: "Protocol Design" },
  { id: "requirements", name: "Requirements & Safety" },
];

const form = reactive({
  title: "",
  category: "",
  description: "",
  duration: null,
  intervention: "",
  measurements: [""],
  timeline: [{ name: "", description: "" }],
  requirements: [""],
  exclusionCriteria: [""],
  safetyMonitoring: "",
});

const addMeasurement = () => form.measurements.push("");
const removeMeasurement = (index) => form.measurements.splice(index, 1);

const addPhase = () => form.timeline.push({ name: "", description: "" });
const removePhase = (index) => form.timeline.splice(index, 1);

const addRequirement = () => form.requirements.push("");
const removeRequirement = (index) => form.requirements.splice(index, 1);

const addExclusionCriteria = () => form.exclusionCriteria.push("");
const removeExclusionCriteria = (index) =>
  form.exclusionCriteria.splice(index, 1);

const submitForm = () => {
  console.log("Form submitted:", form);
  // Add your submission logic here
};
</script>
