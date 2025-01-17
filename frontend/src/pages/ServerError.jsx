const ServerError = () => {
  return (
    <div className='text-center my-3'>
          <h1 className='text-3xl font-medium mt-4 py-3'>Server Error!</h1>
          <div className='py-3 mb-3 md:w-10/12'>
            <p className='text-center px-3'>
              Uh-oh, something went wrong on our end. It seems the server has
              encountered a problem. Don`&apos;`t worry, we are on
              it! Meanwhile, here is a button to help you head back to the home
              page.
            </p>
          </div>
          <button
            className='button btn shadow my-3'
            href='/'
          >
            Back to Home Page
          </button>
    </div>
  );
};

export default ServerError;