from dash import html, dcc

def create_navbar():
    return html.Header([
        dcc.Store(id="local-storage-data", storage_type='local'),

         html.Script("""
    window.addEventListener('storage', function(event) {
        if (event.key === 'selected_marker') {
            const detail = event.newValue || null;
            const customEvent = new CustomEvent("localStorageChanged", { detail });
            document.dispatchEvent(customEvent);
        }
    });

    document.addEventListener("localStorageChanged", function(event) {
        const store = document.querySelector("#local-storage-data");
        if (store) {
            const reactProps = Object.getOwnPropertyDescriptor(store.__proto__, "props");
            if (reactProps && reactProps.get) {
                store.props.setProps({ data: event.detail });
            }
        }
    });
    """),
              html.Div(id="display-data"),
            html.Div("Dashboard World Data 2023"),
            html.Button([
                html.I(className = "fa-solid fa-map-marker-alt")
            ], id="bouton")
        ])
    
    # Dash callback to display data
    @app.callback(
    Output('display-data', 'children'),
    Input('local-storage-data', 'data')
    )  
    def display_local_storage(data):
        if data is None:
            return "No marker selected."
        return f"Selected Marker: {data}"
        