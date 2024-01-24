# Configure custom 404 page
error_page 404 /404.html;

location = /404.html {
    root /var/www/html;
    internal;
    return 404 '<html><head><title>404 Not Found</title></head><body><h1>Ceci n'est pas une page</h1></body></html>';
}
