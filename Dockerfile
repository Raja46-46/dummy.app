# Use the official Nginx image
FROM nginx:alpine

# Copy your HTML file to the Nginx web directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Nginx will start automatically with the container
