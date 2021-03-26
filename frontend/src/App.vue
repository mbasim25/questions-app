<template>
  <div id="app" class=" pb-4 font-serif "  >
       <NavbarComponent />
    <router-view />
  </div>
</template> 

<script>
import { apiService } from "@/common/api.service"
import NavbarComponent from "@/components/Navbar.vue"
export default  {
  name : "App",
  components: {
    NavbarComponent
  },
  methods: {
    async setUserInfo(){
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  created(){
    this.setUserInfo()
  }
}
</script>

<style src="@/assets/css/tailwind.css">


