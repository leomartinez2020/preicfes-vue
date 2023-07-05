<script>
import CuadroOpciones from '@/components/CuadroOpciones.vue'
import CuadroRespuestas from '@/components/CuadroRespuestas.vue'

// import datos from '@/assets/datos1.json'
import datos from '@/assets/datostest.json'

export default {
  components: {
    CuadroOpciones,
    CuadroRespuestas
  },
  data() {
    return {
      was_submitted: false,
      correctResponses: 0,
      responses: {},
      quizzes: datos.quizzes,
    }
  },
  computed: {
    quizId() {
      return parseInt(this.$route.params.id)
    },
    quiz() {
      return this.quizzes.filter(dato => dato.id === this.quizId)[0]
    },
  },
  methods: {
    handleSelected(arg1, arg2) {
      this.responses[arg2] = arg1;
      console.log("emission received", arg1, arg2);
    },
    procesar() {
      for (let key in this.responses) {
         const coco = this.quiz.preguntas.filter(obj => obj.pk === parseInt(key));
         if (coco[0].letra === this.responses[key]) {
           this.correctResponses++;
           coco[0].correct = true;
         }
      }
      this.was_submitted = true;
    }
  }
}
</script>

<template>
<!-- <header class="w-4/5 mx-auto mt-6 flex justify-between"> -->
<header class="w-4/5 mx-auto mt-6 justify-between">
  <h1 class="text-xl text-center font-bold text-yellow-700">{{ quiz.titulo }}</h1>
</header>

<div class="w-4/5 mx-auto pt-8">
<!-- <form @submit.prevent="submit"> -->
  <form v-on:submit.prevent>
  <!-- Seccion tipo 1 -->
  <div v-if="quiz.tipo === 'tipouno'">
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.texto }}</p>
    <div v-if="quiz.descripcion">{{ quiz.descripcion }}</div>
    <p class="font-bold text-2xl text-yellow-700 text-center">{{ quiz.tema }}</p>
    <p><span class="px-2 bg-blue-300 font-bold text-yellow-700 rounded-md">Ejemplo</span></p>
    <p><span class="font-bold">0.</span> {{ quiz.ejempregunta }}</p>
    <!-- Cuadro de opciones para el ejemplo -->
    <CuadroOpciones />
    <section class="my-10 grid grid-cols-2 md:grid-cols-3 gap-4">
      <div class="sm:border-r-4 border-yellow-700 col-span-2">
        <h3 class="text-xl text-amber-700 font-bold border-b-4 border-yellow-700 mr-4">Descripciones</h3>
          <!-- Cuadro de opciones -->
          <div class="pb-4" v-for="(pregunta, index) in quiz.preguntas">
            <p class="">
              <span class="font-bold">{{  index + 1 }}.</span>
              {{ pregunta.texto }}
              <span v-if="was_submitted && pregunta['correct']">&#9989;</span>
              <span v-else-if="was_submitted && !pregunta['correct']">&#10060;</span>
              <span v-else></span>
            </p>
            <CuadroRespuestas :class="[was_submitted ? pregunta['correct'] ? 'submitted-correct' : 'submitted-wrong' : '']" :pk="pregunta.pk" :was_submitted="was_submitted" @selectedLetter="handleSelected"/>
          </div>
          <!-- Fin cuadro de opciones -->
      </div>
      <div class="">
        <h3 class="text-xl text-amber-700 font-bold border-b-4 border-yellow-700">Palabras</h3>
        <div v-for="(value, key, index) in quiz.palabras" :key="index">
          <span v-if="key === 'H'" class="mt-2 p-1 inline-block text-lg font-bold text-yellow-700 rounded-md border-blue-300 bg-blue-300"><span class="font-bold">{{ key }}.</span> {{value}}</span>
          <p v-else class="text-lg py-3"><span class="font-bold">{{ key }}.</span> {{value}}</p>
        </div>
      </div>
    </section>
    <p class="text-xl text-blue-700 text-center"># respuestas correctas: {{ correctResponses }}</p>
  </div>
  <!-- Fin seccion tipo 1 -->

    <!-- Botón enviar -->
    <div class="text-center my-6">
     <button v-if="!was_submitted" @click="procesar" class="cursor-pointer mt-4 text-white bg-blue-300 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4">Evaluar</button>
     <button v-else disabled class="mt-4 text-gray-500 bg-slate-300 text-lg font-medium rounded-lg px-5 px-4">Evaluar</button>
    </div>
  </form>
</div>
</template>

<style>
.submitted-correct {
  background-color: lightgreen;
}

.submitted-wrong {
  background-color: red;
}
</style>
