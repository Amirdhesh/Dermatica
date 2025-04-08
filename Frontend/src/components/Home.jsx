import React, { useRef, useState } from 'react';
import axios from 'axios';

export default function Home() {
    const inputRef = useRef(null);
    const [image, setImage] = useState(null);
    const [response, setresponse] = useState(null);

    const handleClick = () => {
        inputRef.current.click();
    };

    const handleDragOver = (event) => {
        event.preventDefault();
    };

    const handleDrop = (event) => {
        event.preventDefault();
        const file = event.dataTransfer.files[0];
        setImage(file);
    };
    
    const handleFileInputChange = (event) => {
        const file = event.target.files[0];
        setImage(file);
    };

    const handleSubmit = async () => {
        try {
            let formData = new FormData();
            formData.append('file', image);
            const response = await axios.post('http://localhost:8000/api/model', formData, {
            });
            if (response.status === 200) {
                setresponse(response.data)
                console.log("Hello",response)
            }
            setImage(null)
        } catch (error) {
            console.error('Error processing image:', error);
        }
    };

    return (
        <>
        {   response ? 
                <div className='h-screen flex flex-col justify-evenly items-center pt-14'>
                    <div className='flex flex-col justify-center items-center'>
                        <div className=" border-[#5c47e0] w-[550px] h-[550px]  rounded-xl  items-center rounded-5 p-4 pt-10 mt-5 pb-10 border-solid  border-2 bg-gray-50 shadow-lg">
                            <article className='px-5 wrap-break-word'>
                                <h2 className='flex justify-center font-bold text-2xl'>{response.disease}</h2>
                                <p className='text-justify pt-4'>{response.comment}</p>                            
                            </article>
                        </div>
                        <div className='pl-96'>
                            <div onClick={()=>setresponse(null)} className='text-left text-red-500 font-semibold py-3 cursor-pointer hover:text-red-600'>
                                Clear Response
                            </div>
                        </div>
                    </div>
                </div> 
                :
                <div className='h-screen flex flex-col justify-evenly items-center pt-10'>
                <div className='flex flex-col justify-center items-center'>
                    <div className='text-4xl font-bold text-center'>
                        Upload Images
                    </div>
                    <div className='text-center font-semibold py-3'>
                        Related to Skin disease
                    </div>

                    <div onDragOver={handleDragOver} onDrop={handleDrop} onClick={handleClick} className="border-gray-300 w-[450px] h-[324px]  rounded-xl flex flex-col justify-center items-center rounded-5 p-4 pt-10 mt-5 pb-10 border-solid border-8 bg-[#D5CFFE]">
                        {
                            image ? <img src={URL.createObjectURL(image)} alt="Uploaded" className='w-full h-full' /> :
                                <>
                                    <p className='text-[#4C4C4C]'>Click to Upload</p>
                                    <p className='text-[#4C4C4C]'>or</p>
                                    <p className='text-[#4C4C4C]'>Drag and Drop Image here</p>
                                </>
                        }
                        <input type="file" onChange={handleFileInputChange} hidden ref={inputRef}/>
                    </div>
                    <div className='pl-80'>
                        <div onClick={()=>setImage(null)} className='text-left font-semibold py-3 cursor-pointer hover:text-shadow-sm'>
                            Clear selection
                        </div>
                    </div>
                    <div className='flex justify-center items-center'>
                        <button onClick={handleSubmit} className='px-[172px] py-3 rounded-md bg-[#8245E7] text-white font-semibold duration-150 ease-in-out hover:scale-105'>
                            Submit Image
                        </button>
                    </div>
                </div>
            </div>
            
        }

           
            
            <div className='absolute top-[32rem] left-[8rem]'>
                <div className='w-[140px] h-[140px] bg-[#DBDBDB]'></div>
                <div className='w-[140px] h-[140px] bg-[#58FD92] rounded-full -mt-16 ml-12 '></div>
            </div>
            <div className='absolute top-[7rem] right-32'>
                <div className='w-[140px] h-[140px] bg-[#FDCF58] rounded-full '></div>
                <div className='w-[140px] h-[140px] bg-[#58C2FD] rounded-full -mt-20 ml-16 '></div>
            </div>
        </>
    );
}