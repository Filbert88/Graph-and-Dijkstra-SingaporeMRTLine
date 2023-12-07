# Singapore MRT Route Finder

## Overview
This is a project for developer's paper that title **"Efficient Route Mapping in the Singapore MRT Leveraging Graph Theory and Dijkstra's Algorithm"**. This program is implementing Graph and Dijkstra to find the most optimized route.

## Description
The Singapore MRT Route Finder is a Python application designed to find the most optimized route between two MRT (Mass Rapid Transit) stations in Singapore. It considers interchange stations and peak/off-peak hours to suggest the quickest route for your journey. 

## Features
- Finds the shortest path between two MRT stations.
- Considers interchange stations for route optimization.
- User-friendly interface with clear instructions.
- Option to view a list of all MRT stations sorted by line.

## How to Use
1. **Clone/Download the Repository**: 
   - Clone the repository using `git clone https://github.com/Filbert88/Graph-and-Dijkstra-SingaporeMRTLine.git` or download the source code directly from the repository page.

2. **Running the Program**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the program is located.
   - Run the program using the command: 
   ```
   python main.py
   ```
   
3. **Using the Program**:
   - Upon launching, you will be greeted with a welcome message.
   - You can choose to view the list of MRT stations by entering `YES` when prompted.
   - Enter the name of the source MRT station.
   - Enter the name of the destination MRT station.
   - The program will display the most optimized path for your journey.

## Requirements
- Python 3

## Room for Improvement
This program only use a static data and only based on the newest map until December 2023, but it can be improved by using a real-time data for the singapore MRT provided by Singapore's transport authorities or third-party APIs that aggregate transport data.
