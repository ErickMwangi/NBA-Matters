import React, {useEffect, useState} from 'react'
import PlayBoy from './PlayBoy';

function PlayerList() {
  const [data, setData] = useState([]);
  console.log (data)
  useEffect(() => {
    fetch("http://127.0.0.1:5555/players")
    .then(r => r.json())
    .then((data) => setData(data));
  }, []);
  const playa = data.map((item,index)=>
  <PlayBoy key = {index} id = {item.id} name = {item.name} image = {item.image} ranking = {item.ranking} mvp = {item.mvp} />
  )
  return (
    <div>
      {playa}
    </div>

  )
}
export default PlayerList;