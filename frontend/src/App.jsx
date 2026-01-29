import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [produits, setProduits] = useState([])
  const [chargement, setChargement] = useState(true)

  useEffect(() => {
    // Appel à l'API Flask (Système Réparti : Communication entre services)
    axios.get('http://localhost:5000/api/produits')
      .then(response => {
        setProduits(response.data)
        setChargement(false)
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des produits:", error)
        setChargement(false)
      })
  }, [])

  return (
    <div style={{ padding: '40px', textAlign: 'center', fontFamily: 'sans-serif' }}>
      <h1>Ma Boutique Répartie</h1>
      <hr />
      {chargement ? (
        <p>Chargement des données depuis l'API...</p>
      ) : (
        <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', marginTop: '20px' }}>
          {produits.map(produit => (
            <div key={produit.id} style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '8px', width: '200px' }}>
              <h3>{produit.nom}</h3>
              <p>Prix : {produit.prix} FCFA</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App