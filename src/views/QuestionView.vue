<script setup lang="ts">
import { onActivated, onDeactivated, ref } from 'vue'
import * as api from '@/api/api-client';
import type Question from '@/api/question';
import { useRoute } from 'vue-router'
import MarkdownIt from "markdown-it";
import { inject } from 'vue';
import mathjax3 from 'markdown-it-mathjax3';
const spinner = inject('spinner') as {
  loading: boolean
};
const route = useRoute()
const question = ref({} as Question);
const isThreadComplete = ref(true);


const id = Array.isArray(route.params.id) ? route.params.id[0] : route.params.id

spinner.loading = true;
try {
  question.value = await api.getQuestion(id);
} finally {
  spinner.loading = false;
}

onActivated(() => {
  scrollToTop();
  checkIfThreadIsComplete(question.value, true);
})

onDeactivated(() => {
  isThreadComplete.value = true;
})

function scrollToTop() {
  window.scrollTo(0, 0);
}


function checkIfThreadIsComplete(data: Question, forceStart: boolean = false) {
  if (isThreadComplete.value && !forceStart) {
    return
  }

  const oneHour = 3600 * 1000;
  const age = Date.now() - data?.created_date?.getTime();

  const isComplete =
    (data &&
      data.question &&
      (data.posts.length ?? 0) >= data.count) ||
    age >= oneHour;

  isThreadComplete.value = !!isComplete;

  if (!isComplete) {
    setTimeout(pollQuestion, 5000); // retry every 5 seconds
  }
}

async function pollQuestion() {
  try {
    console.log('Polling question...');
    const data = await api.getQuestion(id);
    question.value = data;
    checkIfThreadIsComplete(data);
  } catch (err) {
    console.error('Error polling question:', err);
  }
}

function renderMarkdown(markdown: string): string {
  markdown = markdown.replace(/\\\[(.+?)\\\]/gs, '$$$$$1$$$$');
  markdown = markdown.replace(/\\\((.+?)\\\)/gs, (match, p1) => {
    const cleaned = p1.replace(/[ \t\f\r\v]+/g, '');  // remove spaces, tabs, etc, but NOT \n
    return `$${cleaned}$`;
  });
  markdown = markdown.replace(/(?<!^)\$\$\s*(.+?)\s*\$\$(?!$)/gm, '$$$1$$')
  const markdownIt = new MarkdownIt().use(mathjax3);
  return markdownIt.render(markdown);
}

</script>

<template>
  <div v-if="question.question">
    <div class="user-question">
      <h1>User Asks</h1>
      <div v-html="renderMarkdown(question.question)" />
    </div>
    <hr>
    <div class="conversation">
      <div class="response-row" v-for="item in question.posts">
        <img class="avatar" :src="'./images/avatars/' + item.persona?.toLocaleLowerCase() + '.webp'" alt="avatar">
        <div :class="'response' + ' response-' + item.persona.toLocaleLowerCase().replace(/ /g, '-')">
          <h1>{{ item.persona }}</h1>
          <div class="response-content" v-html="renderMarkdown(item.content)" />
        </div>
      </div>
      <div class="more-wisdom" v-if="!isThreadComplete">
        Wisdom yet lingers still
      </div>
    </div>
  </div>
  <div class="silence" v-else>
    Only the memory of meaning drifts in the dark
  </div>
</template>

<style>
.response-content h1 {
  font-size: 1.5em;
}

.response-content h2 {
  font-size: 1.25em;
}

.response-content h3 {
  font-size: 1em;
}

.response-content h4,
.response-content h5,
.response-content h6 {
  font-size: 1em;
}
</style>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jura:wght@300..700&family=Merienda:wght@300..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&family=Jura:wght@300..700&family=Merienda:wght@300..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cedarville+Cursive&display=swap');

.user-question {}

.conversation {
  display: flex;
  flex-direction: column;
  row-gap: 1em;
}

.response-row {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.response-row h2 {
  margin-top: 0;
  margin-bottom: 0;
}

.response-row {}

.avatar {
  min-width: 8em;
  max-width: 8em;
  margin-right: 1em;
  flex-basis: content;
}

.response-the-cube {
  font-family: "Jura", sans-serif;
}

.response-the-borg-queen {
  font-family: "Orbitron", serif;
}

.response-the-borg-queen h1 {
  color: white;
  text-shadow: 1px 1px 10px greenyellow, 1px 1px 10px green;
}

.response-the-borg-queen div {
  color: greenyellow;
}


.response-jehovah {
  font-family: "Cardo", serif;
  font-size: larger;
}

.response-john-carmack div {
  font-family: "JetBrains Mono", monospace;
}
</style>

<style>
pre {
  font-family: "JetBrains Mono", monospace;
  width: auto;
}


.silence,
.more-wisdom {
  font-style: italic;
  /* Make it fill the viewport */
  width: 100vw;

  /* Use flexbox to center content */
  display: flex;
  justify-content: center;
  /* horizontal centering */
  align-items: center;
  /* vertical centering */

  /* Optional: for text styling */
  text-align: center;
  animation: throb 4s infinite;
}

.silence {
  height: 100vh;
  color: white;
  font-size: xx-large;
  text-shadow: 1px 1px 10px gray, 1px 1px 10px white;
  font-family: "Cedarville Cursive", cursive;
}

p {
  margin-top: 0.5em;
  margin-bottom: 0;
}

@keyframes throb {

  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}
</style>
