<template>
    <div class=" container mx-auto px-24 py-4">
        <div>
            <div>
                <div class="mb-2 inline-flex items-center">
                    <svg class="h-7 w-7  text-gray-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg> 
                    <p class="  text-red-500 tracking-wide mx-1  text-lg"> {{ answer.author }} </p> 
                    
                </div>
               
            </div>
            <div class=" rounded-md py-2  border-2 shadow-md text-gray-700 ">
                <h2 class="  py-4 px-4 text-lg ">{{ answer.body}}</h2>
                <hr class="">
             <div class=" py-2 flex justify-between mr-6 ">
                    <p class="text-base text-gray-700 px-4  ">{{answer.created_at}}</p>
                    <div v-if="isAnswerAuthor">
                        <button class="rounded text-base ml-2"> <router-link
                        :to="{name: 'answer-editor', params: {id: answer.id}}"
                        class="no-underline inline-flex items-center"
                        ><span class="text-gray-800">Edit</span> 
                        <svg class="w-4 h-4 ml-1 text-red-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg> 
                        </router-link>
                        </button>
                    
                        <button
                        @click="triggerDeleteAnswer"
                        class="ml-2 text-red-500 text-base inline-flex items-center "> 
                            <span class="text-gray-800">Delete</span> 
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-4 h-4 ml-1 text-red-500" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                            </svg>
                        </button>
                    </div>
                    <div v-else>
                        <button @click="toggleLike"  class=" ml-2 focus:outline-none  text-base inline-flex items-center "><svg class="h-5 w-5 ml-1 text-red-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                        </svg> ({{ likesCounter }})</button>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template> 

<script>
import { apiService } from "@/common/api.service";
export default { 
    name: "AnswerComponent",
    props: {
        answer:{
            type: Object,
            required: true
        },
        requestUser:{
            type: String,
            required: true
        }
    },
    data(){
        return{
            userLikedAnswer: this.answer.user_has_voted,
            likesCounter: this.answer.likes_count
        }
    },
    computed: {
        isAnswerAuthor(){
            return this.answer.author === this.requestUser;
        }
    },
    methods:{
        toggleLike(){
            this.userLikedAnswer ===false
            ? this.likeAnswer()
            : this.unLikeAnswer()
        },
        likeAnswer(){
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            let endpoint = `/api/answers/${ this.answer.id }/like/`
            apiService(endpoint, "POST")
        },
        unLikeAnswer(){
            this.userLikedAnswer = false;
            this.likesCounter -= 1;
            let endpoint = `/api/answers/${ this.answer.id }/like/`
            apiService(endpoint, "DELETE")

        },
        triggerDeleteAnswer(){
            this.$emit("delete-answer", this.answer)
        }
    }
} 
</script>
