<script>
export default {
  props: ['pk'],
  data() {
        return {
            selectedOption: ''
        }
    }
}
</script>

<template>
    <div class="w-fit m-2 bg-blue-300 p-2 rounded-lg">
    <ul class="p-1 bg-white flex gap-2 border border-yellow-700 rounded-lg">
        <li>
            <input @change="$emit('selectedLetter', 'A', pk)" type="radio" :id="'A-'+pk" :name="'pregunta-'+pk" :value="'A-'+pk" class="hidden peer" required>
            <label :for="'A-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">A</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'B', pk)" type="radio" :id="'B-'+pk" :name="'pregunta-'+pk" :value="'B-'+pk" class="hidden peer" required>
            <label :for="'B-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">B</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'C', pk)" type="radio" :id="'C-'+pk" :name="'pregunta-'+pk" :value="'C-'+pk" class="hidden peer" required>
            <label :for="'C-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">C</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'D', pk)" type="radio" :id="'D-'+pk" :name="'pregunta-'+pk" :value="'D-'+pk" class="hidden peer" required>
            <label :for="'D-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">D</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'E', pk)" type="radio" :id="'E-'+pk" :name="'pregunta-'+pk" :value="'E-'+pk" class="hidden peer" required>
            <label :for="'E-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">E</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'F', pk)" type="radio" :id="'F-'+pk" :name="'pregunta-'+pk" :value="'F-'+pk" class="hidden peer" required>
            <label :for="'F-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">F</div>
            </label>
        </li>
        <li>
            <input @change="$emit('selectedLetter', 'G', pk)" type="radio" :id="'G-'+pk" :name="'pregunta-'+pk" :value="'G-'+pk" class="hidden peer" required>
            <label :for="'G-'+pk" class="flex items-center py-1 px-3 w-full text-yellow-700 bg-white rounded-full border border-yellow-700 cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-yellow-700 peer-checked:bg-blue-300 hover:text-gray-600 hover:bg-blue-200 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-blue-300">
                <div class="text-lg font-semibold">G</div>
            </label>
        </li>
        </ul>
    </div>
</template>
