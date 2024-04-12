import "./Navbar.scss";
export default function Navbar() {
  return (
    <div className="navbar">
      <a
        href="#sidebar"
        className="d-block mt-3"
        data-bs-toggle="offcanvas"
        role="button"
        aria-controls="sidebar"
      >
        <span className="fas fa-bars"></span>
      </a>
      <div
        className="offcanvas offcanvas-start"
        tabIndex="-1"
        id="sidebar"
        aria-labelledby="sidebar-label"
      >
        <div className="offcanvas-header bg-dark text-light options p-0">
          <span className="m-3"></span>
          <h5 className="offcanvas-title text-center" id="sidebar-label">
            <span className="fas text-light">Options</span>
          </h5>
          <button
            type="button"
            className="btn-close btn-close-white"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div className="offcanvas-body navbar navbar-dark bg-dark">
          <ul className="nav flex-column">
            <li className="nav-item">
              <a className="nav-link" href="/profile">
                <span className="fas fa-user">
                  <span className="m-2"></span>Profile
                </span>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/settings">
                <span className="fas fa-cog">
                  <span className="m-2"></span>Setting
                </span>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/logout">
                <span className="fas fa-sign-out-alt">
                  <span className="m-2"></span>Logout
                </span>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <button
        type="button"
        className="btn btn-primary rounded-circle"
        data-bs-toggle="modal"
        data-bs-target="#userprofile"
      >
        <span className="fas fa-user"></span>
      </button>
      <div
        className="modal fade"
        id="userprofile"
        tabIndex="-1"
        aria-labelledby="userprofileLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-dialog-centered" role="document">
          <div className="modal-content">
            <div className="modal-header bg-dark text-light border-0">
              <h5 className="modal-title" id="userprofileLabel">
                Accounts
              </h5>
              <button
                type="button"
                className="btn-close btn-close-white"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className="modal-body bg-dark">
              <ul className="list-group">
                <li className="list-group-item">
                  <span className="fas fa-user"></span>
                  <span className="m-2">Achu</span>
                </li>
                <li className="list-group-item">
                  <span className="fas fa-user"></span>
                  <span className="m-2">Akshith</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
