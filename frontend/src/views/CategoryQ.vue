<template>
  <div class=" grid grid-cols-4 home">
   
    <div class=" col-start-2 col-span-2 -mx-2 my-14  ">
     <div class=" mb-3  bg-gradient-to-r from-gray-100 to-white  rounded-md py-4 px-4 shadow-md  "
          v-for="question in questions "
          :key="question.pk">
          <p class="text-md font-light text-gray-600 pb-2  ">Category :
                <span class=" text-gray-600 ">{{ question.category }}</span>
             </p>
             <hr class="pb-1">
        <p class=" text-md py-2 text-gray-600">posted by :
         <span class=" text-red-500  ">{{ question.author }}</span>
       </p>
       
       <router-link class="  text-2xl  pt-4 " :to="{ name: 'question', params: { slug: question.slug}}">{{ question.content }}</router-link>
       <hr class="mt-3">
       <p class="pt-3 "> Answers : <span class="">{{question.answers_count }}</span></p>
     </div>
     
      
   </div>
  
  </div>
</template>




<script> 
import { apiService } from "@/common/api.service";
export default {
  name: "CategoryQ",
  props:{
      id:{
          type: String,
          required: true
      }
  },
  data(){
    return{
      questions:[],
     
    }
  },
   methods:{
    getQuestions(){
      let endpoint = `/api/category/${this.id}/questions/`;
      apiService(endpoint)
                .then(data => {
                  this.questions.push(...data.results)
                 
                })
    },
   },
   created(){
       this.getQuestions()
   },
};
</script>