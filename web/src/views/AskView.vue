<script setup lang="ts">
import { ref } from 'vue'
import * as api from '@/api/api-client';
import MarkdownIt from 'markdown-it';
import mathjax3 from 'markdown-it-mathjax3';
import { useRouter } from 'vue-router'
const question = ref('');
const errorMessage = ref('');
const router = useRouter()

function renderMarkdown(markdown: string): string {
  const markdownIt = new MarkdownIt().use(mathjax3);
  return markdownIt.render(markdown);
}

async function submitQuestion(): Promise<void> {
  if (!question.value.trim()) {
    errorMessage.value = "Question cannot be empty.";
    return;
  }
  errorMessage.value = "";
  // Emit the question to the parent component or handle it as needed
  let response = await api.submitQuestion(question.value);
  // Clear the input field after submitting
  router.push({ name: 'question', params: { id: response } });
  question.value = "";
}
</script>
<template>
  <h2>Ask The Forum</h2>
  <form @submit.prevent="submitQuestion">
    <div class="form-group">
      <textarea id="question" v-model="question" placeholder="Type your question here..." required></textarea>
      <a href="https://commonmark.org/help/" target="_blank">Markdown Help</a>
    </div>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    <button type="submit">Ask</button>
  </form>
  <fieldset>
    <legend>Preview</legend>
    <h2>User Asks</h2>
    <div class="preview" v-html="renderMarkdown(question)" />
  </fieldset>
</template>
<style scoped>
.question-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  resize: vertical;
  box-sizing: border-box;
}

fieldset {
  border-color: gray;
  border-style: groove;
}

form {
  margin-bottom: 0.5em;
}
</style>
