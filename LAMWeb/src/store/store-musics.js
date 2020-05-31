import Vue from 'vue'
import { uid } from 'quasar'

// The data goes here
const state = {
  musics: {
    1: {
      name: 'Eu navegarei',
      author: 'Gabriela Rocha',
      type1: 'Adoração',
      type2: null,
      type3: null
    },
    2: {
      name: 'Lugar secreto',
      author: 'Gabriela Rocha',
      type1: 'Oração',
      type2: 'Louvor',
      type3: null
    },
    3: {
      name: 'Atos 2',
      author: 'Gabriela Rocha',
      type1: 'Oração',
      type2: 'Júbilo',
      type3: 'Adoração'
    },
    4: {
      name: 'Creio que Tu és a cura',
      author: 'Gabriela Rocha',
      type1: 'Oração',
      type2: 'Adoração',
      type3: null
    }
  }
};

// Contains not assynchronous -> Change state directly
const mutations = {
  updateMusic (state, payload) {
    Object.assign(state.musics[payload.id],payload.updates)
  },
  deleteMusic (state, id) { 
    Vue.delete(state.musics,id)
  },
  createMusic (state, payload) {
    Vue.set(state.musics, payload.id, payload.music)
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  updateMusic ({ commit }, payload) {
    commit('updateMusic', payload)
  },
  deleteMusic ({ commit }, id) {
    commit('deleteMusic', id)
  },
  createMusic ({ commit }, music) {
    let musicId = uid()
    let payload = {
      id: musicId,
      music: music
    }
    commit('createMusic', payload)
  }
};

// Get data from a State
const getters = {
  musics: (state) => {
    return state.musics
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}