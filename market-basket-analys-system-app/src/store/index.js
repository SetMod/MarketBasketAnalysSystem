import { createStore } from 'vuex'
import TransactionsService from '../services/TransactionsService'
// import axios from 'axios';

export default createStore({
  state: {
    transactions: [],
    isLoaded: false,
    errorMsg: "",
    backend_url: "http://127.0.0.1:3000",
  },
  mutations: {
    setTransactions(state, payload) {
      state.transactions = payload.data
    },
    setLoaded(state, payload) {
      state.isLoaded = payload.data
    },
    setError(state, payload) {
      state.errorMsg = payload.data
    },
  },
  actions: {
    getTransactions(context, payload) {
      TransactionsService.getTransactions(context,payload)
    },
  },
  modules: {
  }
})
