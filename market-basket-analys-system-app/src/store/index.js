import { createStore } from 'vuex'
import TransactionsModule from './TransactionsModule'
import AnalyseModule from './AnalyseModule'


export default createStore({
  state: {
    backend_url: "http://127.0.0.1:3000",
  },
  getters: {
    getTransactionsUrl(state){
      return `${state.backend_url}/transactions/pagination?pageSize=${state.transactions.pageSize}&pageNumber=${state.transactions.pageNumber}`
    },
    getTransactionImageUrl(state){
      return `${state.backend_url}/transactions/images/transactions_by_month.png`
    },
    getRulesUrl(state){
      return `${state.backend_url}/transactions/analyse`
    }
  },
  mutations: {
  },
  modules: {
    transactions: TransactionsModule,
    analyse: AnalyseModule
  }
})
