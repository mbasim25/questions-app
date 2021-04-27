<template>
    <div class="container mx-auto px-32 my-12">
        <h1 class="my-4 pt-12 pb-2 mx-12 text-gray-800 text-xl">Edit your Answer!</h1>
        <form @submit.prevent="onSubmit">
            <textarea
            v-model="answerBody"
            class=" shadow-md block border-2  w-full pb-36 px-2 py-2 mx-12 mb-1 text-lg leading-normal border-gray-600 rounded" 
            rows="12"></textarea>
            <br>
            <button type="submit"  class=" hover:bg-red-500   shadow-md p-2 rounded-xl text-base text-red-400 hover:text-gray-50 font-normal tracking-wide mx-12 border-2 border-red-500 border-opacity-60">Publish your answer</button>
        </form>
        <p v-if="error" class=" appearance-none my-2">{{error}}</p>
         <div class="pb-48"></div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service"
export default {
     name: "AnswerEditor",
     props: {
         id:{
             type: Number,
             required: true
         },
         previousAnswer: {
             type: String,
             required: true
         },
         questionSlug: {
             type: String,
             required: true
         }
     },
     data() {
         return{
             answerBody: this.previousAnswer,
             error: null
         }
     },
     methods: {
         onSubmit(){
             if (this.answerBody){
                 let endpoint = `/api/answers/${this.id}/`
                 apiService(endpoint, "PUT", {body: this.answerBody})
                  .then(() =>{
                      this.$router.push({
                      name: "question",
                      params: {slug: this.questionSlug}
                  })
                })
             } else{
                 this.error = "you cant submit an empty answer!"
             }
         }
     },
     async beforeRouteEnter(to, from, next) {
         let endpoint = `/api/answers/${to.params.id}/`;
         let data = await apiService(endpoint);
         to.params.previousAnswer = data.body;
         to.params.questionSlug = data.question_slug;
         return next();
     }
};
</script>