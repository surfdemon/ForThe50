const Forbidden403 = () => {
  return (
    <div className='text-center my-3'>
      <div>
        <div>
          <h1 className='mt-4 py-3'>
            Oops!
          </h1>
          <div className='p-3 mb-3'>
            <p className='text-center px-3'>
              It looks like you’ve stumbled upon restricted area! Don’t worry,
              we added a button to help you get back to home page safely!
            </p>
          </div>
          <div></div>
          <button
            className= 'button btn shadow-xl my-3'
            href='/'
          >
            Back to Home Page
          </button>
        </div>
      </div>
    </div>
  );
};

export default Forbidden403;
