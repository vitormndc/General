using UnityEngine;
using UnityEngine.UI;


public class DrawLine : MonoBehaviour
{
    LineRenderer lineRend;
    float alphaAngle, height, width, slopeLine, btermLine, closestPointX, closestPointY;
    Vector2 point1, point2;
    float lineWidth = 4f;
    bool stopCalc;

    public GameObject cube;
    public GameObject sphere;
    public GameObject redsphere;
    public Text distanceText;

    void Start()
    {
        lineRend = GetComponent<LineRenderer>();
        lineRend.positionCount = 2;

        height = Screen.height;
        width = Screen.width;

        GenerateLine();
        DistPointLine();

        //distance = (pos1 - pos2).magnitude;
    }

    public void GenerateLine()
    {
        stopCalc = true;
        float randHeight = (int)Random.Range(0, height/2);
        float randWidth = (int)Random.Range(0, width);

        point1 = new Vector2((width - randWidth), randHeight);             // Point bellow mid height
        point2 = new Vector2(randWidth, (height - randHeight));            // Point above mid height

        var previousSpheres = GameObject.FindGameObjectsWithTag("spheres");
        foreach (var i in previousSpheres)
        {
            Destroy(i);
        }


        Instantiate(sphere, point1, transform.rotation);
        Instantiate(sphere, point2, transform.rotation);

        float deltaX = point2.x - point1.x;
        float deltaY = point2.y - point1.y;

        slopeLine = deltaY / deltaX;
        btermLine = point1.y - (slopeLine * point1.x);
        lineRend.startWidth = lineWidth;
        lineRend.endWidth = lineWidth;

        lineRend.SetPosition(0, new Vector2(-1*(btermLine/slopeLine), 0));
        lineRend.SetPosition(1, new Vector2((height - btermLine)/slopeLine, height));
        stopCalc = false;
    }

    public void DistPointLine()
    {
        var previousRedSpheres = GameObject.FindGameObjectsWithTag("redSphere");
        foreach (var i in previousRedSpheres)
        {
                Destroy(i);
        }



        float cubeX = cube.transform.position.x;
        float cubeY = cube.transform.position.y;

        float deltaXCubeToP1 = cubeX - point1.x;
        float deltaYCubeToP1 = cubeY - point1.y;

        float distPos1Cube = Mathf.Sqrt(Mathf.Pow((deltaXCubeToP1), 2)+Mathf.Pow((deltaYCubeToP1), 2));
        float anglePos1Cube = Mathf.Atan((cubeY - point1.y) / (cubeX - point1.x));
        float angleLine = Mathf.Atan((point2.y - point1.y) / (point2.x - point1.x));

        anglePos1Cube = ConvertAngleToPositive(anglePos1Cube);
        angleLine = ConvertAngleToPositive(angleLine);

        if (anglePos1Cube > angleLine)                       // if Point is above the line, you need to subtract its angle by the line angle to get the angle inside the triangle
        {
            alphaAngle = anglePos1Cube - angleLine;
        }
        else                                                //if it's bellow you need to subtract the anlge of the line by it's angle
        {
            alphaAngle = angleLine - anglePos1Cube;
        }

        float shortestDistance = distPos1Cube * Mathf.Sin(alphaAngle); 
        distanceText.text = shortestDistance.ToString("F2");

        float slopePerpendicular = -1 * Mathf.Tan(Mathf.PI/2 - angleLine);
        float btermPerpendicular = cubeY - (cubeX * slopePerpendicular);

        float deltaXCubeToLine = Mathf.Sqrt(Mathf.Pow(shortestDistance, 2)/(Mathf.Pow(slopePerpendicular, 2)+1));

        closestPointX = cubeX - deltaXCubeToLine;
        closestPointY = cubeY - deltaXCubeToLine * slopePerpendicular;

        float functionY = closestPointX * slopeLine + btermLine;

        if (Mathf.Ceil(closestPointY) != Mathf.Ceil(functionY)) //This checks if the closest point is at the right direction, if it isn't, the direction is changed
        {
            closestPointX = cubeX + deltaXCubeToLine;
            closestPointY = cubeY + deltaXCubeToLine * slopePerpendicular;
        }


        Instantiate(redsphere, new Vector3(closestPointX, closestPointY, 0), transform.rotation);

    }

    float ConvertAngleToPositive(float angle)
    {
        while (angle < 0)
        {
            angle = angle + Mathf.PI;
        }

        return angle;
    }
    private void FixedUpdate()
    {
        if (!stopCalc)
        {
            DistPointLine();
        }
        
    }

}
