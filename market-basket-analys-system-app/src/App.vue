<template>
  <div class="nav justify-content-center nav-tabs mt-2 mb-5">
    <router-link class="nav-item nav-link" to="/">Home</router-link>
    <router-link class="nav-item nav-link" to="/about">About</router-link>
    <router-link class="nav-item nav-link" to="/transactions"
      >Transactions</router-link
    >
  </div>
  <router-view class="container text-center" />
</template>

<style>
.nav a.router-link-exact-active {
  color: #42b983;
}
</style>
