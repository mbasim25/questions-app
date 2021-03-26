<template>
    <div class="">
        <button class="rounded text-base ml-2  "> <router-link
        :to="{name: 'question-editor', params: {slug: slug}}" class="no-underline inline-flex items-center"><span class="text-gray-800">Edit</span><svg class="w-4 h-4 ml-1 text-red-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
</svg> </router-link></button>
       
        <button
        @click="deleteQuestion" class="  ml-2  text-red-500 text-base inline-flex items-center "> <span class="text-gray-800">Delete</span> <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-4 h-4 ml-1 text-red-500" stroke="currentColor">
           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
               </svg>
              
       </button>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service"
export default {
    name: "QuestionsActions",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    methods: {
        async deleteQuestion(){
            let endpoint = `/api/questions/${this.slug}/`;
            try{
                await apiService(endpoint, "DELETE");
                this.$router.push("/");
            }
            catch (err){
                console.log(err);
            }
        }
    } 
}
</script>

<style scoped>

</style>