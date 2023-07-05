<script>
import datos from '@/assets/datostest.json'

export default {
  async mounted() {
      const file = this.quiz.file;
      const url = `${this.publicPath}/${file}`;
      // console.log(url);
      try {
        const fetchResponse = await fetch(
          url
       )
        .then(response => response.text())
        // .then(data => {console.log(data); this.quiz.lectura = data;});
        .then(data => {this.quiz.lectura = data;});
        //.then(data => {console.log(data);});
      } catch (ex) {
        console.log("Error in fetch");
      }    
  },
  data() {
    return {
      publicPath: import.meta.env.VITE_BASE_URL,
      quizzes: datos.quizzes,
      responses: {},
      correctResponses: 0,
      was_submitted: false,
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
    onChange(arg1, arg2) {
      this.responses[arg1] = arg2;
      console.log(this.responses);
    },
    procesar() {
      for (let key in this.responses) {
         const coco = this.quiz.preguntas.filter(obj => obj.pk === parseInt(key));
         if (coco[0].correct === this.responses[key]) {
           this.correctResponses++;
         }
      }
      this.was_submitted = true;
    }
  }
}
</script>

<template>
<!-- Seccion tipo 2 lectura -->
  <div v-if="quiz.tipo == 'tipolectura'">
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.titulo }}</p>
    <p class="font-bold text-xl text-yellow-700 text-center">{{ quiz.texto }}</p>
    <div>{{ quiz.descripcion }}</div>
    <div class="seccion-lectura">
      <div class="font-serif" v-html="quiz.lectura"></div>
    </div>
    <div v-for="pregunta in quiz.preguntas">
      <!-- Definir las columnas -->
      <!-- <section class="flex justify-between mt-10"> -->
      <section class="mt-6 pb-2 px-2 border-b-4 border-r-4 border-slate-300 shadow-md grid grid-cols-5">
        <p class="mt-1 numeral">
          <span class="font-bold">{{ pregunta.pk }}.</span>
          <span v-if="was_submitted && pregunta['correct'] === responses[pregunta.pk]">&#9989;</span>
          <span v-else-if="was_submitted && pregunta['correct'] !== responses[pregunta.pk]">&#10060;</span>
          <span v-else></span>
        </p>
        <div v-for="opcion in pregunta.opciones">
          <div class="mr-4">
            <input :disabled="was_submitted" @change="onChange(pregunta.pk, opcion)" type="radio" :id="opcion+pregunta.pk" :name="pregunta.pk" :value="opcion+pregunta.pk">
            <label class="m-2" :for="opcion">{{ opcion }}</label>
          </div>
        </div>
      </section>
    </div>
<!-- Fin seccion tipo 2 lectura -->

</div>
<div class="text-center my-6">
  <p>{{ correctResponses }}</p>
  <button v-if="!was_submitted" @click="procesar" class="cursor-pointer mt-4 text-white bg-blue-300 hover:bg-slate-800 text-lg font-medium rounded-lg px-5 focus:ring-4 focus:ring-blue-300 px-4">Revisar</button>
  <button v-else disabled class="mt-4 text-gray-500 bg-slate-300 text-lg font-medium rounded-lg px-5 px-4">Revisar</button>
</div>
</template>

<style>
.seccion-lectura {
  width: 70%;
  margin: auto;
  padding: 12px;
  border: solid brown 2px;
  border-radius: 1rem;
}

.seccion-lectura h2 {
  text-align: center;
}

.seccion-lectura p {
  margin: 6px 0;
}

.numeral {
  width: min-content;
}
</style>
