```bash
# Check Colima disk usage
colima status
docker system df

# Prune unused Docker cache, images and volumes
docker system prune -af --volumes

# Resize Colima's VM disk
colima stop
colima start --disk 100
```
