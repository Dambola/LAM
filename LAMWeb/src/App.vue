<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  methods : {
    mounted() {
      reloadUser();
    }
  }
}
</script>
