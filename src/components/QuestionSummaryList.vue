<script setup lang="ts">
import type QuestionSummary from '@/api/question-summary';
defineProps<{
  questions: QuestionSummary[]
}>()
</script>
<template>
  <ul>
    <li v-for="(item, index) in questions">
      <router-link :to="{ name: 'question', params: { id: item.id } }">{{ item.question
      }}</router-link>
    </li>
  </ul>
</template>
<style scoped>
ul {
  list-style-type: none;
  padding-left: 0.25em;
}

li {
  width: 95%;
  white-space: nowrap;
  overflow: hidden !important;
  text-overflow: ellipsis;
  border: 1px;
  border-color: #404040;
  border-top-style: solid;
  margin-top: 0.25em;
  background: linear-gradient(5deg, #000000 0%, #1a1a1a 100%);
  border-radius: 1px;
}

li:nth-child(2n) {}

a {
  text-decoration: none;
  border-left-style: solid;
  border-left-color: green;
  padding-left: 0.25em;
}

a:visited {
  border-left-color: red;
  color: lightskyblue
}

a:hover {
  color: #ffffff;
}
</style>
