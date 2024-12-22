<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- Progress Header -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold text-neutral-900">
          Join Study: {{ study.title }}
        </h1>
        <div class="text-sm text-neutral-500">Step {{ currentStep }} of 4</div>
      </div>
      <!-- Progress bar -->
      <div class="mt-4 h-2 bg-neutral-100 rounded-full">
        <div
          class="h-2 bg-primary-600 rounded-full transition-all duration-300"
          :style="{ width: `${(currentStep / 4) * 100}%` }"
        ></div>
      </div>
    </div>

    <!-- Step Content -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <!-- Step 1: Study Overview -->
      <div v-if="currentStep === 1">
        <h2 class="text-xl font-semibold mb-6">Study Overview</h2>

        <div class="space-y-6">
          <!-- Key Details -->
          <div class="grid grid-cols-2 gap-4">
            <div class="p-4 bg-neutral-50 rounded-lg">
              <div class="text-sm text-neutral-600">Duration</div>
              <div class="text-lg font-medium">{{ study.duration }} weeks</div>
            </div>
            <div class="p-4 bg-neutral-50 rounded-lg">
              <div class="text-sm text-neutral-600">Time Commitment</div>
              <div class="text-lg font-medium">
                ~{{ study.timeCommitment }} per week
              </div>
            </div>
          </div>

          <!-- Requirements -->
          <div>
            <h3 class="text-lg font-medium mb-3">Requirements</h3>
            <ul class="space-y-2">
              <li
                v-for="req in study.requirements"
                :key="req"
                class="flex items-start"
              >
                <svg
                  class="h-5 w-5 text-primary-600 mr-2 mt-0.5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M5 13l4 4L19 7"
                  />
                </svg>
                {{ req }}
              </li>
            </ul>
          </div>

          <!-- Cost -->
          <div>
            <h3 class="text-lg font-medium mb-3">Estimated Costs</h3>
            <div class="space-y-2">
              <div
                v-for="(cost, type) in study.costs"
                :key="type"
                class="flex justify-between"
              >
                <span class="text-neutral-600">{{ type }}</span>
                <span class="font-medium">${{ cost }}</span>
              </div>
              <div class="border-t pt-2 mt-2">
                <div class="flex justify-between font-medium">
                  <span>Total Estimated Cost</span>
                  <span>${{ totalCost }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Step 2: Eligibility Check -->
      <div v-if="currentStep === 2">
        <h2 class="text-xl font-semibold mb-6">Eligibility Check</h2>

        <div class="space-y-6">
          <div
            v-for="(question, index) in eligibilityQuestions"
            :key="index"
            class="border-b pb-6"
          >
            <div class="text-neutral-900 font-medium mb-2">
              {{ question.text }}
            </div>
            <div class="space-x-4">
              <label class="inline-flex items-center">
                <input
                  type="radio"
                  :name="`question-${index}`"
                  value="yes"
                  v-model="eligibilityAnswers[index]"
                  class="form-radio h-4 w-4 text-primary-600"
                />
                <span class="ml-2">Yes</span>
              </label>
              <label class="inline-flex items-center">
                <input
                  type="radio"
                  :name="`question-${index}`"
                  value="no"
                  v-model="eligibilityAnswers[index]"
                  class="form-radio h-4 w-4 text-primary-600"
                />
                <span class="ml-2">No</span>
              </label>
            </div>
          </div>
        </div>
      </div>

      <!-- Step 3: Data Collection Agreement -->
      <div v-if="currentStep === 3">
        <h2 class="text-xl font-semibold mb-6">Data Collection Agreement</h2>

        <div class="space-y-6">
          <div class="bg-neutral-50 p-4 rounded-lg space-y-4">
            <h3 class="font-medium">Required Measurements</h3>
            <ul class="space-y-2">
              <li
                v-for="measurement in study.measurements"
                :key="measurement.name"
                class="flex items-start"
              >
                <svg
                  class="h-5 w-5 text-neutral-500 mr-2 mt-0.5"
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
                <div>
                  <div class="font-medium">{{ measurement.name }}</div>
                  <div class="text-sm text-neutral-600">
                    {{ measurement.frequency }}
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <div class="space-y-4">
            <h3 class="font-medium">Data Usage Agreement</h3>
            <div class="text-sm text-neutral-600 space-y-2">
              <p>By participating in this study, you agree that:</p>
              <ul class="list-disc pl-5 space-y-1">
                <li>
                  Your anonymized data will be shared with other participants
                </li>
                <li>Aggregate results will be publicly available</li>
                <li>You can withdraw from the study at any time</li>
                <li>Your personal information will remain confidential</li>
              </ul>
            </div>
            <label class="flex items-start mt-4">
              <input
                type="checkbox"
                v-model="dataAgreement"
                class="form-checkbox h-4 w-4 mt-1 text-primary-600"
              />
              <span class="ml-2 text-sm text-neutral-600">
                I understand and agree to the data collection and usage terms
              </span>
            </label>
          </div>
        </div>
      </div>

      <!-- Step 4: Confirmation -->
      <div v-if="currentStep === 4">
        <h2 class="text-xl font-semibold mb-6">Confirm Participation</h2>

        <div class="space-y-6">
          <!-- Summary -->
          <div class="bg-neutral-50 p-4 rounded-lg space-y-4">
            <h3 class="font-medium">Study Summary</h3>
            <dl class="space-y-2">
              <div class="flex justify-between">
                <dt class="text-neutral-600">Start Date</dt>
                <dd class="font-medium">{{ startDate }}</dd>
              </div>
              <div class="flex justify-between">
                <dt class="text-neutral-600">Duration</dt>
                <dd class="font-medium">{{ study.duration }} weeks</dd>
              </div>
              <div class="flex justify-between">
                <dt class="text-neutral-600">Total Cost</dt>
                <dd class="font-medium">${{ totalCost }}</dd>
              </div>
            </dl>
          </div>

          <!-- Final Agreement -->
          <div class="space-y-4">
            <label class="flex items-start">
              <input
                type="checkbox"
                v-model="finalAgreement"
                class="form-checkbox h-4 w-4 mt-1 text-primary-600"
              />
              <span class="ml-2 text-sm text-neutral-600">
                I confirm that I meet all eligibility requirements and commit to
                following the study protocol
              </span>
            </label>
          </div>
        </div>
      </div>

      <!-- Navigation Buttons -->
      <div class="mt-8 flex justify-between">
        <button
          v-if="currentStep > 1"
          @click="currentStep--"
          class="px-4 py-2 border border-neutral-300 rounded-md shadow-sm text-sm font-medium text-neutral-700 bg-white hover:bg-neutral-50"
        >
          Back
        </button>
        <div v-else class="w-20"></div>

        <button
          v-if="currentStep < 4"
          @click="currentStep++"
          class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700"
          :disabled="!canProceed"
        >
          Continue
        </button>
        <button
          v-else
          @click="joinStudy"
          class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary-600 hover:bg-primary-700"
          :disabled="!finalAgreement"
        >
          Join Study
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const currentStep = ref(1);
const dataAgreement = ref(false);
const finalAgreement = ref(false);
const eligibilityAnswers = ref([]);

// Sample study data
const study = {
  title: "Vitamin D Optimization Protocol",
  duration: 12,
  timeCommitment: "30 minutes",
  requirements: [
    "Age 18-65",
    "No current Vitamin D supplementation",
    "Ability to complete blood tests at specified intervals",
    "No history of hypercalcemia",
  ],
  costs: {
    "Blood Tests (3x)": 180,
    Supplements: 45,
    "Lab Processing": 75,
  },
  measurements: [
    { name: "Blood Vitamin D Levels", frequency: "Every 6 weeks" },
    { name: "Supplement Compliance Log", frequency: "Daily" },
    { name: "Symptoms Questionnaire", frequency: "Weekly" },
  ],
};

const eligibilityQuestions = [
  { text: "Are you between 18-65 years old?" },
  { text: "Are you currently free from any serious medical conditions?" },
  { text: "Can you commit to the full 12-week duration?" },
  { text: "Are you willing to complete all required measurements?" },
];

const totalCost = computed(() => {
  return Object.values(study.costs).reduce((a, b) => a + b, 0);
});

const startDate = computed(() => {
  const date = new Date();
  date.setDate(date.getDate() + 14); // Start in 2 weeks
  return date.toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
  });
});

const canProceed = computed(() => {
  if (currentStep.value === 2) {
    return (
      eligibilityAnswers.value.length === eligibilityQuestions.length &&
      eligibilityAnswers.value.every((answer) => answer === "yes")
    );
  }
  if (currentStep.value === 3) {
    return dataAgreement.value;
  }
  return true;
});

const joinStudy = () => {
  // Add join study logic here
  console.log("Joining study...");
};
</script>
