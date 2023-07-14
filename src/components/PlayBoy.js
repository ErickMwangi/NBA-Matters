import React from 'react'

function PlayBoy({id, name, image, ranking, mvp}) {
  return (
    <div>
        {/* <p>{id}</p> */}
        <p>{name}</p>
        <img src={image} alt="Player Art" />
        <p>{ranking}</p>
        <p>{mvp}</p>
    </div>
  )
}
export default PlayBoy;