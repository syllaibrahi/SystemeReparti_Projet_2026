import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [produits, setProduits] = useState([])
  const [chargement, setChargement] = useState(true)
  const [erreur, setErreur] = useState(null)

  useEffect(() => {
    // --- CONFIGURATION CRUCIALE POUR MINIKUBE ---
    // On utilise l'IP et le port Backend vus sur ta capture d'écran
    const BACKEND_URL = 'http://192.168.49.2:31584/api/produits';

    console.log("Tentative de connexion au backend sur :", BACKEND_URL);

    axios.get(BACKEND_URL)
      .then(response => {
        console.log("Données reçues avec succès !", response.data);
        setProduits(response.data);
        setChargement(false);
        setErreur(null);
      })
      .catch(error => {
        console.error("Erreur de connexion :", error);
        setErreur("Impossible de contacter le Backend (Port 31584). Vérifiez que le Pod Flask est Running.");
        setChargement(false);
      });
  }, [])

  return (
    <div className="min-h-screen bg-slate-50 font-sans">
      {/* Navbar */}
      <nav className="bg-indigo-700 p-4 shadow-xl text-white">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-black tracking-tighter">🚀 ELITE-MARKET</h1>
          <div className="flex items-center gap-3">
            <div className={`h-3 w-3 rounded-full ${erreur ? 'bg-red-500' : 'bg-green-400 animate-pulse'}`}></div>
            <span className="text-xs font-bold uppercase tracking-widest opacity-80">
              {erreur ? 'Offline' : 'Système Réparti Actif'}
            </span>
          </div>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-12">
        <header className="mb-16 text-center">
          <h2 className="text-5xl font-extrabold text-slate-900 mb-4">Nos Produits</h2>
          <p className="text-slate-500 text-lg max-w-2xl mx-auto">
            Interface React connectée à une API Flask et une base de données PostgreSQL sur Kubernetes.
          </p>
        </header>

        {/* Affichage des Erreurs */}
        {erreur && (
          <div className="max-w-2xl mx-auto mb-10 bg-red-100 border-2 border-red-200 text-red-700 px-6 py-4 rounded-2xl shadow-sm flex items-center gap-4">
            <span className="text-2xl"></span>
            <p className="font-semibold">{erreur}</p>
          </div>
        )}

        {chargement ? (
          <div className="flex flex-col justify-center items-center h-64">
            <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-indigo-600 border-opacity-20 border-t-indigo-600 mb-4"></div>
            <p className="text-indigo-600 font-medium tracking-wide">Chargement des microservices...</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            {produits.map(produit => (
              <div key={produit.id} className="group bg-white rounded-[2rem] shadow-sm border border-slate-100 p-8 hover:shadow-2xl transition-all duration-500 hover:-translate-y-2">
                <div className="w-full h-52 bg-slate-50 rounded-[1.5rem] mb-6 flex items-center justify-center group-hover:bg-indigo-50 transition-colors">
                   <span className="text-7xl group-hover:scale-110 transition-transform duration-500">📦</span>
                </div>
                
                <h3 className="text-2xl font-bold text-slate-800 mb-1">{produit.nom}</h3>
                <p className="text-slate-400 text-sm mb-4 uppercase tracking-widest font-semibold">Référence #{produit.id}</p>
                
                <div className="flex justify-between items-center mt-6">
                  <p className="text-indigo-600 font-black text-3xl">
                    {produit.prix.toLocaleString()} <span className="text-sm font-bold text-slate-400 uppercase">FCFA</span>
                  </p>
                  <button className="bg-slate-900 hover:bg-indigo-600 text-white p-4 rounded-2xl transition-all active:scale-90 shadow-lg shadow-slate-200">
                    🛒
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <footer className="mt-24 py-12 border-t border-slate-200 bg-white">
        <div className="container mx-auto px-4 text-center">
          <p className="text-slate-500 font-bold mb-2">Projet de Systèmes Répartis - 2026</p>
          <p className="text-slate-400 text-sm italic">Déployé sur HP EliteBook 745 G4 par Ibrahima</p>
        </div>
      </footer>
    </div>
  )
}

export default App