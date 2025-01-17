const NotFound = () => {
  return (
    <div className='mx-auto my-3'>
      <div className='text-center'>
        <h1 className='mt-4 py-3'>Not Found!</h1>
        <div className='py-3 mb-3'>
          <p className="text-center px-3">
            Looks like we could not find the page you were looking for. While we keep
            looking for it, here is a button to help you head back to home page!
          </p>
        </div>
        <button
          className='button btn shadow my-3'
          href='/'
        >
          Back to Home Page
        </button>
      </div>
    </div>
  );
};

export default NotFound;