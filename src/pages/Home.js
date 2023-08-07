import React, { useState } from 'react';
import './Home.css' ; 

function Home() {

  const [name , SetName]= useState ('');
  const [email , SetEmail]= useState ('');
  const handleNameChange = (e) => {
    SetName(e.target.value);
  };

  const handleEmailChange = (e) => {
    SetEmail(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('  http://localhost:5000/cadastros', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email }),
      });

      if (response.ok) {
        console.log('Dados enviados com sucesso!');
        SetName('');
        SetEmail('');
      } else {
        console.error('Erro ao enviar os dados');
      }
    } catch (error) {
      console.error('Erro:', error);
    }
  


  };
  return (
    <div className=' App-header' >
      <h1>Bem-vindo ao App de Saúde e Fitness!</h1>
      <p>Comece sua jornada para um estilo de vida mais saudável.</p>
      
      <div className='signup-form'>
        
        <h2>
            Cadraste-se 
        </h2>
         <form >
         <label  htmlFor='name' >NOME </label>
         <input type='text' id='name' name='name'  value={name}
            onChange={handleNameChange} ></input>
         <label htmlFor='email' > E-mail</label>
         <input type='email' id='email' name='email ' value={email}
            onChange={handleEmailChange} ></input>
         <button type='submit' > Cadastrar </button>

         </form>
      </div>
      <div className='imagen'>
      <img  src= 'fitines.png'
         alt="Mundo Fitness"
         className="fitness-image"
        
        />
      </div>
    </div>
  );
}

export default Home;