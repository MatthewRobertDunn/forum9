<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Spinner from '@/components/Spinner.vue'
import { inject } from 'vue';
const spinner = inject('spinner') as {
  loading: boolean
};
</script>

<template>
  <div class="title-bar">
    <h1><router-link :to="{ name: 'home' }">Forum9</router-link></h1>
    <h2><router-link :to="{ name: 'ask' }">Ask The Forum</router-link></h2>
  </div>
  <div class="quote">
    <span>Your Troubling Ethical Dilemmas Are Meaningless</span>
  </div>
  <RouterView v-slot="{ Component }">
    <template v-if="Component">
      <KeepAlive>
        <Suspense>
          <component :is="Component" :key="$route.fullPath"></component>
        </Suspense>
      </KeepAlive>
    </template>
  </RouterView>
  <!-- loading state -->
  <template v-if="spinner.loading">
    <Spinner></Spinner>
  </template>
</template>

<style scoped>
@font-face {
  font-family: dseg7classic;
  src: url('./fonts/DSEG7Classic-Regular.woff2');
}

.title-bar {
  display: flex;
  justify-content: center;
  /* Center the first item */
  align-items: center;
  /* Align items vertically if necessary */
  position: relative;
  /* Allow positioning of the first item */

}


.title-bar {
  display: flex;
  column-gap: 3em;
  background: linear-gradient(135deg, #2d2d2d, #4b4b4b, #2d2d2d);
  border-bottom: 2px solid #1a1a1a;
  color: #ffffff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
  height: auto;
}

.title-bar h1 {
  font-size: 3em;
}

h1,
h2 {
  margin: 0;
}

h2 {
  text-decoration: underline;
}

h1>a {
  font-size: inherit;
  font-weight: inherit;
  text-decoration: inherit;
  color: inherit;
}


h2>a {
  font-size: inherit;
  font-weight: inherit;
  text-decoration: inherit;
  color: inherit;
}

.counter {
  font-family: 'dseg7classic';
  border-style: inset;
  color: greenyellow;
  padding: 0.1em;

}

.quote {
  display: flex;
  font-style: italic;
  font-weight: lighter;
  justify-content: center;
}
</style>