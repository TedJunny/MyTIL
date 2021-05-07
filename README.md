# MyTIL
Document repository what I learned everyday
==============

하이어라키 뷰에 나열된 순서대로 렌더링 된다. 즉, 하이어라키 뷰에서 위쪽에 있는 요소가 먼저(안쪽에) 렌더링되고 하이어라키 뷰에서 아래쪽에 있는 요소가 나중에(앞쪽에) 렌더링된다. 이러한 렌더링 순서는 UI가 부모 자식의 계층 형태를 이루고 있을 때도 동일하게 적용되며, 자식 요소는 부모 요소보다 나중에 렌더링된다.

렌더링 순서는 하이어라키 뷰에서 설정할 수도 있고, 스크립트를 통해 제어할 수도 있다. Transform 클래스(또는 이 클래스를 상속한 클래스인 RectTransform 클래스)에 포함된 메서드를 사용한다.

```csharp
// obj가 현재 위치한 계층에서 가장 먼저 렌더링되도록 한다
obj.transform.SetAsFirstSibling();

// obj가 현재 위치한 계층에서 가장 나중에 렌더링되도록 한다
obj.transform.SetAsLastSibling();

//obj를 현재 위치한 계층에서 3번째 요소가 되는 위치에 놓는다.
obj.transform.SetSiblingIndex(2);
```

**Screen Space - Camera 모드**

캔버스가 지정된 카메라와 일정 거리만큼 떨어진 앞쪽 위치에 배치되고, 카메라에 의해 렌더링 된다. 화면(게임 뷰)의 크기나 해상도과 변경되거나 카메라의 뷰 포트가 달라지면 이에 맞춰 캔버스도 카메라를 정면으로 바라보도록 크기와 위치, 방향이 자동으로 변경된다.

Render Camera - 캔버스를 렌더링할 카메라를 지정한다.

Plane Distance - 카메라에서 캔버스까지의 거리를 설정한다.

Sorting Layer - 소팅 레이어란 2D 스프라이트를 포함한 2D 그래픽을 렌더링하는 순서를 제어하는 기능을 말한다. 

Order In Layer - 동일 소팅 레이어 안에서 렌더링 되는 요소의 순서를 정할 때 Order In Layer를 사용한다.
