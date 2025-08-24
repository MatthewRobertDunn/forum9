<script setup lang="ts">
import { ref } from 'vue'
import * as api from '@/api/api-client';
import type QuestionSummary from '@/api/question-summary';
import QuestionSummaryList from '@/components/QuestionSummaryList.vue';
import { useRouter, useRoute } from 'vue-router';
import { inject } from 'vue';
const spinner = inject('spinner') as {
  loading: boolean
};
const questions = ref([] as QuestionSummary[]);
const route = useRoute()
const router = useRouter();
const currentDate = route.query.next ? new Date(route.query.next as string) : null;
spinner.loading = true;
try {
  questions.value = await api.getQuestions(currentDate);
} finally {
  spinner.loading = false;
}
const qs = questions.value;
const nextDate = qs.length > 0 ? qs[qs.length - 1].created_date.toISOString() : null;

function pageBack() {
  router.back();
}

</script>
<template>
  <h2>Latest Questions</h2>
  <QuestionSummaryList :questions="questions" />
  <div class="pagination">
    <span>
      <a v-if="currentDate" @click.prevent="pageBack();" href="#">Back</a>
      <a v-if="!currentDate" class="disabled" tabindex="-1" href="#">Back</a>
    </span>
    <span>
      <router-link v-if="nextDate" :to="{ name: 'home', query: { next: nextDate } }">Next</router-link>
    </span>
  </div>
</template>

<style scoped>
.pagination {
  display: flex;
  justify-content: space-around;
}

.pagination a {
  text-align: center;
  font-weight: bold;
  color: white;
}



a.disabled {
  color: gray;
  pointer-events: none;
}

button {
  width: 6em;
}
</style>