<template>
  <div class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container-fluid">
      <a href="/" class="navbar-brand">MBAS</a>
      <div
        class="collapse navbar-collapse justify-content-center"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav me-auto mb-2 mb-sm-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/transactions"
              >Transactions</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about">About</router-link>
          </li>
        </ul>
        <form>
          <input
            class="form-control"
            type="text"
            placeholder="Search"
            aria-label="Search"
          />
        </form>
      </div>
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
    </div>
  </div>
  <router-view class="container" />
</template>

<style>
.nav a.router-link-exact-active {
  color: #42b983;
}
</style>
