//
//  main.cpp
//  498R
//
//  Created by Amy Desposorio on 10/19/19.
//  Copyright © 2019 Amy Desposorio. All rights reserved.
//
#include <iostream> //include libraries up here like importing in python
#include <math.h> //just in case need pow somewhere. to implement: pow(base,exponent) eg. 10e6 is pow(10,6)
#include <fstream>
#include <vector>

using namespace std;

double euls(float dt, float xoriginal){
    double xnew = (1-3*dt)*xoriginal;
    return xnew;
}

int main(int argc, char* argv[]) {
    fstream params;
    vector <float> t ; //vectors over arrays
    vector <float> x ;
    float dt = 0;
    float steps = 0;
    string filename(argv[1]); //"shift - command - <" opens up this here
    params.open(filename);
    params>> dt; //params points to dt and in Slurm will be adjusted to 10^-6, 10^-5, 10^-4 ..
    dt = atof(argv[1]); //casted char to float
    steps = 9.0/dt;
    x.resize(steps+2);
    t.resize(steps+2);
    
    float xnew=1; //start at (t,x) = (0,1)
    for (int i=0; i<steps+1; i++){
        x.at(i) = xnew;
        xnew = euls(dt,x.at(i));
        t.at(i+1) = t.at(i) + dt;
        cout << "t=" << t.at(i) << "," << "x=" << x.at(i) << ";" << endl;

}
        ofstream myfile;
        myfile.open ("/Users/damym/datafortraining.txt");
    for(int j=0; j<steps; j++){
        myfile << x[j] << endl;
    }
        myfile.close();
        return 0;
}

//Bash and Slurm idea: for loop with i and j; do and end are i.e. the {}'s ~/Users/damym/datatfortraining1.txt
