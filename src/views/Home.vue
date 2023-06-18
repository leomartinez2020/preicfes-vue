<template>
    <div class="">
      <h1 class="text-3xl font-bold text-blue-700">Todas las actividades</h1>
      <router-link
        v-for="dato in datos"
        :key="dato.id"
        :to="dato.slug"
      >
        <h2 class="my-4 hover:text-blue-300 hover:font-bold">{{ dato.titulo }}</h2>
      </router-link>  
    </div>
</template>

<script>
import datos from '@/assets/datos1.json'

export default {
    data() {
        return {
            datos: datos.quizzes
        }
    }
}
</script>
