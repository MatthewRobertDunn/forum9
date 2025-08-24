import { type App, reactive } from 'vue';

const loadingState = reactive({ loading: false });

const SpinnerPlugin = {
  install(app: App) {
    app.config.globalProperties.$loading = loadingState;
    app.provide('spinner', loadingState);
  }
};

export default SpinnerPlugin;