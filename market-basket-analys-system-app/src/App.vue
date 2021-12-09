<template>
  <div class="nav navbar-expand-sm navbar-light nav-tabs mt-1">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse justify-content-center"
        id="navbarSupportedContent"
      >
        <router-link class="nav-item nav-link" to="/">Home</router-link>
        <router-link class="nav-item nav-link" to="/transactions"
          >Transactions</router-link
        >
        <router-link class="nav-item nav-link" to="/about">About</router-link>
      </div>
    </div>
  </div>
  <router-view class="container" />
</template>

<style>
.nav a.router-link-exact-active {
  color: #42b983;
}
</style>
