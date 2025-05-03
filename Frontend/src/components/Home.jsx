import React, { useRef, useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

export default function Home() {
    const inputRef = useRef(null);
    const [image, setImage] = useState(null);
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false); // <- NEW STATE

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
        if (!image) return; // Guard against empty submission
        try {
            setLoading(true); // <- SET LOADING TRUE
            let formData = new FormData();
            formData.append('file', image);
            const response = await axios.post('http://localhost:8000/api/model', formData);
            if (response.status === 200) {
                setResponse(response.data);
            }
            setImage(null);
        } catch (error) {
            console.error('Error processing image:', error);
        } finally {
            setLoading(false); // <- SET LOADING FALSE
        }
    };

    return (
        <>
            {loading ? (
                // LOADING UI
                <div className='min-h-screen flex flex-col justify-center items-center'>
                    <div className='text-xl font-semibold text-gray-700 animate-pulse'>
                        Processing your image...
                    </div>
                </div>
            ) : response ? (
                <div className='min-h-screen flex flex-col justify-evenly items-center pt-14 px-4'>
                    <div className='flex flex-col justify-center items-center w-full max-w-4xl'>
                        <div className="border-[#5c47e0] w-full max-w-[550px] h-[550px] rounded-xl border-2 border-solid shadow-lg bg-blue-50 overflow-hidden">
                            <div className="h-full p-4 pt-10 pb-10 overflow-y-auto 
                                [&::-webkit-scrollbar]:w-1.5 
                                [&::-webkit-scrollbar-track]:bg-transparent 
                                [&::-webkit-scrollbar-thumb]:bg-gray-100 
                                [&::-webkit-scrollbar-thumb]:rounded-full 
                                hover:[&::-webkit-scrollbar-thumb]:bg-gray-400">
                                <article className='px-5 break-words'>
                                    <h2 className='flex justify-center font-bold text-2xl'>{response.disease}</h2>
                                    <div className='text-justify pt-4 prose max-w-none'>
                                        <ReactMarkdown>{response.comment}</ReactMarkdown>
                                    </div>
                                </article>
                            </div>
                        </div>
                        <div className='w-full max-w-[550px] flex justify-end'>
                            <div onClick={() => setResponse(null)} className='text-left text-red-500 font-semibold py-3 cursor-pointer hover:text-red-600'>
                                Clear Response
                            </div>
                        </div>
                    </div>
                </div>
            ) : (
                <div className='min-h-screen flex flex-col justify-evenly items-center pt-10 px-4'>
                    <div className='flex flex-col justify-center items-center w-full max-w-4xl'>
                        <div className='text-3xl md:text-4xl font-bold text-center'>
                            Upload Images
                        </div>
                        <div className='text-center font-semibold py-3'>
                            Related to Skin disease
                        </div>

                        <div 
                            onDragOver={handleDragOver} 
                            onDrop={handleDrop} 
                            onClick={handleClick} 
                            className="border-gray-300 w-full max-w-[450px] h-[300px] md:h-[324px] rounded-xl flex flex-col justify-center items-center p-4 pt-10 mt-5 pb-10 border-solid border-8 bg-[#D5CFFE]"
                        >
                            {image ? (
                                <img src={URL.createObjectURL(image)} alt="Uploaded" className='w-full h-full object-contain' />
                            ) : (
                                <>
                                    <p className='text-[#4C4C4C]'>Click to Upload</p>
                                    <p className='text-[#4C4C4C]'>or</p>
                                    <p className='text-[#4C4C4C]'>Drag and Drop Image here</p>
                                </>
                            )}
                            <input type="file" onChange={handleFileInputChange} hidden ref={inputRef} />
                        </div>
                        <div className='w-full max-w-[450px] flex justify-end'>
                            <div onClick={() => setImage(null)} className='text-left font-semibold py-3 cursor-pointer hover:text-shadow-sm'>
                                Clear selection
                            </div>
                        </div>
                        <div className='flex justify-center items-center w-full max-w-[450px]'>
                            <button 
                                onClick={handleSubmit} 
                                className='w-full py-3 rounded-md bg-[#8245E7] text-white font-semibold duration-150 ease-in-out hover:scale-105'
                                disabled={!image} // Optional: disable button if no image
                            >
                                Submit Image
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Decorative elements - hidden on small screens */}
            <div className='hidden md:block absolute top-[32rem] left-[2rem] lg:left-[8rem]'>
                <div className='w-[100px] lg:w-[140px] h-[100px] lg:h-[140px] bg-[#DBDBDB]'></div>
                <div className='w-[100px] lg:w-[140px] h-[100px] lg:h-[140px] bg-[#58FD92] rounded-full -mt-12 lg:-mt-16 ml-8 lg:ml-12'></div>
            </div>
            <div className='hidden md:block absolute top-[7rem] right-4 lg:right-32'>
                <div className='w-[100px] lg:w-[140px] h-[100px] lg:h-[140px] bg-[#FDCF58] rounded-full'></div>
                <div className='w-[100px] lg:w-[140px] h-[100px] lg:h-[140px] bg-[#58C2FD] rounded-full -mt-12 lg:-mt-20 ml-12 lg:ml-16'></div>
            </div>
        </>
    );
}
