<template>
    <div class="my-12 container mx-auto px-64  ">
        <div v-if="question" >
            <div class="  pb-6  ">
             <div class="mb-3   rounded-md py-4 px-2 border-2 shadow-md">
                 <p class=" text-lg py-2 text-gray-800 pl-2">Author :
                 <span class=" text-red-500  ">{{ question.author }}</span>
                  </p>
                 <h1 class=" block px-2 py-2 break-normal mb-1 text-xl leading-normal">{{question.content}}</h1>
                  <hr class="my-3"> 
                  <div class="flex justify-between mr-6">
                     <p class="text-md font-normal tracking-wide  px-2 text-gray-600 ">Posted at: {{question.created_at}}</p> 
                     <QuestionActions
                       v-if="isQuestionAuthor"
                       :slug="question.slug" />
                   </div>
                </div>
            </div>
            
       <div v-if="userHasAnswered"  >
           <p class=" text-blue-400 ml-2">You've Already Written an Answer!</p>
       </div>
       
       <div v-else-if="showForm" class="  pb-12 px-20" >
           <form @submit.prevent="onSubmit">
               <div class="mt-2 my-2 tracking-wide  text-lg ">Answer the Question</div>
               <div >
                   <textarea 
                   class="w-full px-2 py-2 mb-1 text-lg border-2 bg-gray-50 border-gray-300 focus:border-gray-500 rounded"
                   rows="7"
                   v-model="newAnswerBody"
                   placeholder="share your thoughts!"></textarea>
               </div>
               <div class="">
                   <button type="submit" class="  hover:bg-red-500   shadow-md p-1.5 rounded-xl text-base text-red-400 hover:text-gray-50 font-normal tracking-wider  border-2 border-red-500 border-opacity-60">Submit</button>
               </div>
           </form>
           <p v-if="error" class="my-2">{{error}}</p>
       </div>
       <div v-else class=" ">
           <div class="">
            <div class="inline-flex ml-3 mb-4">
                <p>have anything to share ? </p>
               <button
               class=" text-blue-400 "
               @click="showForm = true"
               >Add an Answer</button>
            </div>
           </div>
       </div>
        </div>
        <div v-else>
             <h1>404 - Question Not Found</h1>
        </div>

        <div v-if="question" class="">
            <AnswerComponent
            v-for="answer in answers"
            :answer="answer"
            :requestUser="requestUser"
            :key="answer.id" 
            @delete-answer="deleteAnswer"
            /> 
       
        <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
        v-show="next"
        @click="getQuestionAnswers"
        class=" hover:bg-red-500   shadow-md p-2 rounded-xl text-base text-red-400 hover:text-gray-50 font-normal tracking-wide mx-12 border-2 border-red-500 border-opacity-60">Load More</button>
      </div> 
      </div>
    </div>
  
</template>

<script>
import { apiService } from "@/common/api.service"
import AnswerComponent from "../components/Answer.vue"
import QuestionActions from '../components/QuestionActions.vue'
export default {
   name: "Question",
   props: {
       slug: {
           type: String,
           required: true
       }
   },
   components: {
       AnswerComponent,
       QuestionActions
   }, 
   data() {
       return {
           question: {},
           answers: [],
           newAnswerBody: null,
           error: null,
           userHasAnswered: false,
           showForm: false,
           next: null,
           loadingAnswers : false,
           requestUser: null
       }
   },
    computed: {
        isQuestionAuthor(){
            return this.question.author === this.requestUser;
        }
    },
   methods: {
       setPageTitle(title){
            document.title = title;
       },
       setRequestUser(){
           this.requestUser = window.localStorage.getItem("username");
       },
       getQuestionData() {
           let endpoint = `/api/questions/${this.slug}/`;
           apiService(endpoint)
                    .then(data => {
                        if (data){
                         this.question = data;
                         this.userHasAnswered = data.user_has_answered;
                         this.setPageTitle(data.content)
                        } else{
                            this.question = null;
                            this.setPageTitle("404 - Page Not Found")
                        }
                       
                    })
       },
      
       getQuestionAnswers(){
           let endpoint = `/api/questions/${this.slug}/answers/`;
           if (this.next){
               endpoint = this.next;
           }
           this.loadingAnswers = true;
           apiService(endpoint)
             .then(data => {
                 this.answers.push(...data.results);
                 this.loadingAnswers = false;
                  if(data.next){
                    this.next = data.next;
                  } else {
                    this.next = null;
                  }
             })
       },
      
           
       onSubmit(){
           if (this.newAnswerBody){
             let endpoint = `/api/questions/${this.slug}/answer/`;
             apiService(endpoint, "POST", {body: this.newAnswerBody})
             .then(data => {
                 this.answers.unshift(data)
             })
             this.newAnswerBody = null;
             this.showForm = false;
             this.userHasAnswered = true;
             if (this.error){
                 this.error = null;
             }
           } else {
               this.error = "you cant send and empty answer!";
           }
       },
       async deleteAnswer(answer){
           let endpoint = `/api/answers/${answer.id}/`;
           try {
               await apiService(endpoint, "DELETE")
               this.$delete(this.answers, this.answers.indexOf(answer))
               this.userHasAnswered = false;
           }
           catch (err){
               console.log(err)
           }
           
       }
   },
   created() {
       this.getQuestionData() 
       this.getQuestionAnswers()
       this.setRequestUser()
   }
}
</script>

<style>

</style>
