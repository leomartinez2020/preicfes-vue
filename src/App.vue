<script>
import LecturaCompo from './components/LecturaCompo.vue';
export default {
  components: {
    LecturaCompo
  }
}
</script>

<template>
  <nav class="text-blue-700 text-xl text-center mx-auto font-bold underline h-16 bg-sky-300">
    <router-link to="/" class="align-middle">Home</router-link>
  </nav>
  <!-- <div class="container mx-auto w-96"> -->
  <div class="container mx-auto">
    <router-view></router-view>
  </div>
</template>

<style scoped>

</style>
